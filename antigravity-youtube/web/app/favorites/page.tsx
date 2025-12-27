import { fetchArticles } from '@/lib/feishu';
import FavoritesList from '@/components/FavoritesList';

export default async function FavoritesPage() {
    const articles = await fetchArticles();

    return (
        <main className="min-h-screen bg-[#F8F9FA]">
            <FavoritesList articles={articles} />
        </main>
    );
}
