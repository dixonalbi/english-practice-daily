import { Link } from "@tanstack/react-router";

export function NotFound() {
  return (
    <div className="mx-auto max-w-3xl px-6 py-32 text-center">
      <p className="eyebrow mb-6">404 — page missing</p>
      <h1 className="display text-6xl tracking-tight mb-6">
        Wrong shelf.
      </h1>
      <p className="text-ink-muted mb-10">
        Whatever you were looking for isn&rsquo;t in this stack.
      </p>
      <Link
        to="/"
        className="text-sm underline underline-offset-4 hover:text-accent"
      >
        Back to the index
      </Link>
    </div>
  );
}
