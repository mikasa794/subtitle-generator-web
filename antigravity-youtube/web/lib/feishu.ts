
const APP_ID = process.env.FEISHU_APP_ID || 'cli_a9c6a1bb56f89cd4';
const APP_SECRET = process.env.FEISHU_APP_SECRET || 'Ox6v51RIbon1bbxaHmvUGhqRNnW3CiUs';
const APP_TOKEN = process.env.FEISHU_APP_TOKEN || 'FCnWb734NawZW6spPVvcMjtonjf';
const TABLE_ID = process.env.FEISHU_TABLE_ID || 'tblZh4KDjOUZnpod'; // Articles Table
const COURSES_TABLE_ID = 'tbleFDCQBG74x5sp';
const LESSONS_TABLE_ID = 'tbl04aHyg3FzM5sQ';

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
}

async function getTenantAccessToken() {
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
            };
        });

    } catch (error) {
        console.error('Error fetching lessons:', error);
        return [];
    }
}
