import { fetchArticles } from '@/lib/feishu';
import ArticleFeed from '@/components/ArticleFeed';
import Link from 'next/link';

export default async function Home() {
  const articles = await fetchArticles();

  return (
    <main className="min-h-screen bg-[#F5F5F7]">
      <ArticleFeed articles={articles} />
    </main>
  );
}
