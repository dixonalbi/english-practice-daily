import { Outlet } from "@tanstack/react-router";
import { Header } from "@/src/components/layout/Header";

export function RootLayout() {
  return (
    <div className="min-h-full flex flex-col bg-paper text-ink">
      <Header />
      <main className="relative z-10 flex-1">
        <Outlet />
      </main>
      <footer className="relative z-10 border-t border-rule mt-24">
        <div className="mx-auto max-w-6xl px-6 py-10 flex flex-wrap items-baseline justify-between gap-4">
          <p className="eyebrow">Quiet Library — local · v0.1</p>
          <p className="text-sm text-ink-muted">
            Built for focused practice. Progress saved on this device.
          </p>
        </div>
      </footer>
    </div>
  );
}
