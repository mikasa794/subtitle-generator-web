export const CATEGORY_TAGS = [
    'All',
    'New',
    'AI Coding',
    'AI Products',
    'AI Organization',
    'AI Business',
    'AI Principles',
    'Personal Productivity',
    'Physical AI'
];

const TAG_MAPPING: Record<string, string> = {
    'AI应用': 'AI Products',
    '大模型': 'AI Principles',
    '创业故事': 'AI Business',
    '精选': 'AI Principles',
    '趋势': 'New',
    '物理AI': 'Physical AI',
    '具身智能': 'Physical AI',
    'SaaS': 'AI Business',
    '编程': 'AI Coding',
    '效率': 'Personal Productivity',
    '默认': 'AI Products' // Fallback
};

export function mapTagToEnglish(chineseTag: string): string {
    // If it's already an English tag in our list, return it
    if (CATEGORY_TAGS.includes(chineseTag)) return chineseTag;

    // Lookup mapping
    return TAG_MAPPING[chineseTag] || chineseTag;
}

export function getAllTags(): string[] {
    return CATEGORY_TAGS;
}
