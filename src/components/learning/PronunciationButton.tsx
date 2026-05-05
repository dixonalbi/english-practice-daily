
import { Volume2 } from "lucide-react";
import { useState } from "react";
import { cn } from "@/src/lib/utils";
import { container } from "@/src/lib/di/container";

interface Props {
  text: string;
  className?: string;
  size?: "sm" | "md";
  label?: string;
}

export function PronunciationButton({ text, className, size = "sm", label }: Props) {
  const [pulse, setPulse] = useState(false);

  function handleClick(e: React.MouseEvent) {
    e.stopPropagation();
    container.speech.speak(text);
    setPulse(true);
    setTimeout(() => setPulse(false), 380);
  }

  const dimension = size === "sm" ? "h-7 w-7" : "h-10 w-10";
  const icon = size === "sm" ? 13 : 16;

  return (
    <button
      type="button"
      onClick={handleClick}
      aria-label={label ?? `Listen: ${text}`}
      className={cn(
        "inline-flex items-center justify-center rounded-full border border-rule text-ink-muted hover:text-accent hover:border-accent transition-colors",
        dimension,
        pulse && "animate-[ping_0.4s_ease-out]",
        className,
      )}
    >
      <Volume2 size={icon} />
    </button>
  );
}
