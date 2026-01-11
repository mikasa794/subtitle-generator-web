
const APP_ID = process.env.FEISHU_APP_ID || 'cli_a9c6a1bb56f89cd4';
// Cache Buster: 1
const APP_SECRET = process.env.FEISHU_APP_SECRET || 'Ox6v51RIbon1bbxaHmvUGhqRNnW3CiUs';
const APP_TOKEN = process.env.FEISHU_APP_TOKEN || 'FCnWb734NawZW6spPVvcMjtonjf';
const TABLE_ID = process.env.FEISHU_TABLE_ID || 'tblZh4KDjOUZnpod'; // Articles Table
const COURSES_TABLE_ID = 'tbleFDCQBG74x5sp';
const LESSONS_TABLE_ID = 'tbl04aHyg3FzM5sQ';
const LINGO_TABLE_ID = 'tblTEYjEp8ZtDwZZ';
const VOCAB_TABLE_ID = 'tblMYEUusOpQ9HIN'; // User Vocabulary V2 Table

interface VocabPayload {
    word: string;
    meaning: string;
    context: string;
    videoTitle: string;
    videoUrl: string;
    timestamp: number;
}

export async function saveVocab(payload: VocabPayload) {
    try {
        const token = await getTenantAccessToken();
        const url = `https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${VOCAB_TABLE_ID}/records`;

        const fields = {
            "Word": payload.word,
            "Meaning": payload.meaning,
            "Context Sentence": payload.context,
            "Video Title": payload.videoTitle,
            "Video URL": { link: payload.videoUrl, text: "View Video" },
            "Timestamp": payload.timestamp,
            "Saved Date": Date.now(),
            "Review Count": 0
        };

        const res = await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ fields })
        });

        const data = await res.json();
        if (data.code === 0) {
            return { success: true, id: data.data.record.record_id };
        } else {
            console.error('Feishu Save Error:', data);
            return { success: false, error: data.msg };
        }
    } catch (e) {
        console.error('Save Vocab Exception:', e);
        return { success: false, error: 'Internal Error' };
    }
}

export async function getVocabList() {

    try {
        const token = await getTenantAccessToken();
        // Sort by Saved Date DESC
        const url = `https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${VOCAB_TABLE_ID}/records?sort=["Saved Date DESC"]&page_size=100`;

        const res = await fetch(url, {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        const data = await res.json();
        if (data.code === 0) {
            return {
                success: true,
                items: data.data.items.map((item: any) => ({
                    id: item.record_id,
                    word: item.fields["Word"],
                    meaning: item.fields["Meaning"],
                    context: item.fields["Context Sentence"],
                    videoTitle: item.fields["Video Title"],
                    videoUrl: item.fields["Video URL"]?.link,
                    timestamp: item.fields["Timestamp"]
                }))
            };
        }
        return { success: false, error: data.msg };
    } catch (e) {
        return { success: false, error: 'Fetch Exception' };
    }
}

export interface Article {
    id: string;
    title: string;
    summary: string;
    cover?: string;
    date: string;
    author: string;
    tags: string[];
    goldenQuote: string;
    url: string;
}

export interface Course {
    id: string;
    title: string;
    description: string;
    cover?: string;
    status: 'Generating' | 'Done';
}

export interface Lesson {
    id: string;
    title: string;
    moduleTitle: string;
    videoUrl: string;
    duration: string;
    courseId: string;
    transcript?: string;
}

export interface LingoClip {
    id: string;
    title: string;
    series: string;
    targetLang: string;
    videoUrl: string;
    transcript: string;
    difficulty: string;
    aiNotes?: string;
    status: string;
    cover?: string;
}

export async function getTenantAccessToken() {
    const res = await fetch('https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            app_id: APP_ID,
            app_secret: APP_SECRET,
        }),
        cache: 'no-store',
    });

    const data = await res.json();
    if (data.code !== 0) {
        throw new Error(`Failed to get access token: ${data.msg}`);
    }
    return data.tenant_access_token;
}

export async function fetchArticles(): Promise<Article[]> {
    try {
        const token = await getTenantAccessToken();

        // Construct query parameters
        const params = new URLSearchParams({
            filter: 'CurrentValue.[Status]="Done"',
            sort: '["Date DESC"]',
        });

        const res = await fetch(`https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${TABLE_ID}/records?${params}`, {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
            next: { revalidate: 60 }, // Cache for 1 minute
        });

        const data = await res.json();
        if (data.code !== 0) {
            console.error('Feishu API Error:', data);
            return [];
        }

        if (!data.data?.items) return [];

        return data.data.items.map((item: any) => {
            const f = item.fields;
            return {
                id: item.record_id,
                title: f['Title'] || 'Untitled',
                summary: f['Summary'] || '',
                // Handle attachment array for cover
                cover: f['Cover'] && f['Cover'][0] ? f['Cover'][0].url : undefined,
                date: f['Date'] ? new Date(f['Date']).toISOString().split('T')[0] : '',
                author: f['Author'] || '',
                tags: f['Tags'] || [],
                goldenQuote: f['Golden Quote'] || '',
                // Handle link object for URL
                url: f['URL'] ? f['URL'].link : '',
            };
        });
    } catch (error) {
        console.error('Error fetching articles:', error);
        return [];
    }
}

export async function fetchArticleById(id: string): Promise<Article | null> {
    const articles = await fetchArticles();
    return articles.find(a => a.id === id) || null;
}

export async function fetchCourses(): Promise<Course[]> {
    try {
        const token = await getTenantAccessToken();
        const res = await fetch(`https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${COURSES_TABLE_ID}/records`, {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
            next: { revalidate: 10 }, // Short cache for status updates
        });

        const data = await res.json();
        if (data.code !== 0) {
            console.error('Feishu API Error (Courses):', data);
            return [];
        }

        if (!data.data?.items) return [];

        return data.data.items.map((item: any) => {
            const f = item.fields;
            return {
                id: item.record_id,
                title: f['Title'] || 'Untitled Course',
                description: f['Description'] || '',
                // Check Attachment 'Cover' first, then Text 'Cover Image URL'
                cover: (f['Cover'] && f['Cover'][0] ? f['Cover'][0].url : undefined) || f['Cover Image URL'],
                status: f['Status'] || 'Generating',
            };
        });

    } catch (error) {
        console.error('Error fetching courses:', error);
        return [];
    }
}

export async function fetchLessons(courseId: string): Promise<Lesson[]> {
    try {
        const token = await getTenantAccessToken();
        // Filter by Course ID
        const params = new URLSearchParams({
            filter: `CurrentValue.[Course ID]="${courseId}"`,
            // Optional: Sort by Sort Order if we had it populated
        });

        const res = await fetch(`https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${LESSONS_TABLE_ID}/records?${params}`, {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
            next: { revalidate: 60 },
        });

        const data = await res.json();
        if (data.code !== 0) {
            console.error('Feishu API Error (Lessons):', data);
            return [];
        }

        if (!data.data?.items) return [];

        return data.data.items.map((item: any) => {
            const f = item.fields;
            return {
                id: item.record_id,
                title: f['Title'] || 'Untitled Lesson',
                moduleTitle: f['Module Title'] || '',
                videoUrl: f['Video URL'] ? f['Video URL'].link : '',
                duration: f['Duration'] || '',
                courseId: f['Course ID'] || '',
                transcript: f['Transcript'] || '',
            };
        });

    } catch (error) {
        console.error('Error fetching lessons:', error);
        return [];
    }
}

export async function fetchLingoClips(series?: string): Promise<LingoClip[]> {
    try {
        const token = await getTenantAccessToken();
        let params = new URLSearchParams();
        if (series) {
            params.append('filter', `CurrentValue.[Series]="${series}"`);
        }

        const res = await fetch(`https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${LINGO_TABLE_ID}/records?${params}`, {
            headers: { 'Authorization': `Bearer ${token}` },
            next: { revalidate: 10 },
        });

        const data = await res.json();
        if (data.code !== 0) return [];
        if (!data.data?.items) return [];

        // Helper to fetch JSON from attachment URL
        const fetchTranscriptJson = async (url: string) => {
            try {
                // Try with Auth first (Standard for Bitable API)
                let res = await fetch(url, { headers: { 'Authorization': `Bearer ${token}` } });

                // If 403/400, try without (CDN signed link might reject Auth header)
                if (!res.ok) {
                    console.warn(`Fetch with auth failed (${res.status}), retrying without headers...`);
                    res = await fetch(url);
                }

                if (res.ok) {
                    const text = await res.text();
                    return text;
                } else {
                    console.error(`Failed to fetch transcript file: ${res.status} ${res.statusText}`);
                }
            } catch (e) { console.error("Failed to fetch transcript json exception", e); }
            return '';
        };

        const items = await Promise.all(data.data.items.map(async (item: any) => {
            const f = item.fields;
            let transcriptJson = f['Transcript'] || '';

            // Check for JSON file in 'Transcript File' attachment (Prioritized)
            // Fallback to 'Cover' if needed (for legacy), but 'Transcript File' is the new standard.
            let attachmentField = f['Transcript File'];
            if (!attachmentField && f['Cover']) attachmentField = f['Cover']; // Fallback

            if (attachmentField && Array.isArray(attachmentField)) {
                const jsonFile = attachmentField.find((a: any) => a.name.endsWith('.json'));
                if (jsonFile && jsonFile.url) {
                    const fetched = await fetchTranscriptJson(jsonFile.url);
                    if (fetched) transcriptJson = fetched;
                }
            }

            return {
                id: item.record_id,
                title: f['Title'] || 'Untitled',
                series: f['Series'] || '',
                targetLang: f['Target Language'] || 'English',
                cover: f['Cover Image URL'] || (f['Cover Image'] && f['Cover Image'][0] ? f['Cover Image'][0].url : undefined) || (f['Cover'] && f['Cover'][0] ? f['Cover'][0].url : undefined),
                videoUrl: f['Video URL'] ? f['Video URL'].link : '',
                transcript: transcriptJson,
                difficulty: f['Difficulty'] || 'Intermediate',
                aiNotes: f['AI Notes'] || '',
                status: f['Status'] || 'Done',
            };
        }));

        return items;
    } catch (error) {
        console.error('Error fetching lingo clips:', error);
        return [];
    }
}
