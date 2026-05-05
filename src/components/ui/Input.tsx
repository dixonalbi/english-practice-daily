import { forwardRef, type InputHTMLAttributes } from "react";
import { cn } from "@/src/lib/utils";

export const Input = forwardRef<HTMLInputElement, InputHTMLAttributes<HTMLInputElement>>(
  function Input({ className, ...rest }, ref) {
    return (
      <input
        ref={ref}
        className={cn(
          "h-11 w-full bg-paper-card border border-rule-strong rounded-sm px-3 font-sans text-[15px] text-ink placeholder:text-ink-faint focus:outline-none focus:border-accent focus:ring-2 focus:ring-accent-bg",
          className,
        )}
        {...rest}
      />
    );
  },
);
