import { Link } from "@tanstack/react-router";
import { ArrowUpRight, type LucideIcon } from "lucide-react";
import { cn } from "@/src/lib/utils";

interface Props {
  to?: string;
  number: string;
  title: string;
  description: string;
  meta: string;
  icon?: LucideIcon;
  disabled?: boolean;
}

export function PracticeModeCard({
  to,
  number,
  title,
  description,
  meta,
  icon: Icon,
  disabled,
}: Props) {
  const className = cn(
    "group relative block bg-paper-card border border-rule rounded-sm p-6 transition-all hover:shadow-card-hover hover:-translate-y-0.5 hover:border-rule-strong",
    disabled && "opacity-50 pointer-events-none",
  );

  const content = (
    <>
      <div className="flex items-start justify-between mb-8">
        <span className="font-mono text-[11px] tnum text-ink-faint">{number}</span>
        <ArrowUpRight
          size={14}
          className="text-ink-faint group-hover:text-accent group-hover:rotate-12 transition-all"
        />
      </div>
      <h3 className="display text-2xl mb-2 leading-tight">{title}</h3>
      <p className="text-sm text-ink-muted leading-relaxed mb-6">{description}</p>
      <div className="flex items-center justify-between pt-4 border-t border-rule">
        {Icon ? <Icon size={14} className="text-ink-faint" /> : <span />}
        <span className="eyebrow">{meta}</span>
      </div>
    </>
  );

  if (disabled || !to) {
    return <div className={className}>{content}</div>;
  }
  return (
    <Link to={to} className={className}>
      {content}
    </Link>
  );
}
