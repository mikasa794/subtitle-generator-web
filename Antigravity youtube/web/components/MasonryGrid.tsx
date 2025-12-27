export default function MasonryGrid({ children }: { children: React.ReactNode }) {
    return (
        <div className="columns-1 md:columns-2 lg:columns-3 xl:columns-4 2xl:columns-5 gap-6 space-y-6 p-4 md:p-0">
            {children}
        </div>
    );
}
