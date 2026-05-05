import { Link, useLocation } from "@tanstack/react-router";
import { Moon, Sun, BookMarked } from "lucide-react";
import { useSyncExternalStore } from "react";
import { cn } from "@/src/lib/utils";

const NAV = [
  { to: "/", label: "Index" },
  { to: "/verbs", label: "Verbs" },
  { to: "/prepositions", label: "Prepositions" },
  { to: "/phrasal-verbs", label: "Phrasal" },
  { to: "/everyday", label: "Everyday" },
] as const;

const themeListeners = new Set<() => void>();
function subscribeTheme(cb: () => void) {
  themeListeners.add(cb);
  return () => themeListeners.delete(cb);
}
function readTheme(): boolean {
  if (typeof document === "undefined") return false;
  return document.documentElement.classList.contains("dark");
}

function useDarkTheme(): [boolean, () => void] {
  const dark = useSyncExternalStore(subscribeTheme, readTheme, () => false);
  const toggle = () => {
    const next = !document.documentElement.classList.contains("dark");
    document.documentElement.classList.toggle("dark", next);
    try {
      localStorage.setItem("quietlibrary:theme", next ? "dark" : "light");
    } catch {}
    for (const l of themeListeners) l();
  };
  return [dark, toggle];
}

export function Header() {
  const { pathname } = useLocation();
  const [dark, toggleTheme] = useDarkTheme();

  function isActive(to: string): boolean {
    return to === "/" ? pathname === "/" : pathname.startsWith(to);
  }

  return (
    <header className="sticky top-0 z-20 border-b border-rule bg-paper/80 backdrop-blur">
      <div className="mx-auto max-w-6xl px-6 h-16 flex items-center gap-8">
        <Link to="/" className="flex items-center gap-2 group">
          <BookMarked
            size={16}
            className="text-accent transition-transform group-hover:-rotate-6"
          />
          <span className="display text-[19px] tracking-tight">Quiet Library</span>
        </Link>

        <nav className="hidden md:flex items-center gap-6 ms-auto">
          {NAV.map((item, i) => {
            const active = isActive(item.to);
            return (
              <Link
                key={item.to}
                to={item.to}
                className={cn(
                  "text-sm tracking-wide transition-colors",
                  active ? "text-ink" : "text-ink-muted hover:text-ink",
                )}
              >
                <span className="font-mono text-[10px] me-2 text-ink-faint tnum">
                  0{i + 1}
                </span>
                {item.label}
                {active && <span className="block h-px bg-accent mt-0.5" aria-hidden />}
              </Link>
            );
          })}
        </nav>

        <button
          type="button"
          onClick={toggleTheme}
          aria-label="Toggle theme"
          className="ms-auto md:ms-0 h-9 w-9 inline-flex items-center justify-center rounded-sm border border-rule hover:border-rule-strong transition-colors text-ink cursor-pointer"
        >
          {dark ? <Sun size={15} /> : <Moon size={15} />}
        </button>
      </div>

      <div className="md:hidden border-t border-rule">
        <div className="mx-auto max-w-6xl px-6 py-2 flex gap-4 overflow-x-auto">
          {NAV.map((item) => {
            const active = isActive(item.to);
            return (
              <Link
                key={item.to}
                to={item.to}
                className={cn(
                  "text-xs whitespace-nowrap py-1 transition-colors",
                  active ? "text-ink border-b border-accent" : "text-ink-muted",
                )}
              >
                {item.label}
              </Link>
            );
          })}
        </div>
      </div>
    </header>
  );
}
