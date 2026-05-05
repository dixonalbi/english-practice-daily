import { cva, type VariantProps } from "class-variance-authority";
import { forwardRef, type ButtonHTMLAttributes } from "react";
import { cn } from "@/src/lib/utils";

const button = cva(
  "inline-flex items-center justify-center gap-2 select-none whitespace-nowrap font-sans text-sm transition-[background,color,border,transform] duration-200 disabled:opacity-40 disabled:cursor-not-allowed focus-visible:outline-2 focus-visible:outline-accent focus-visible:outline-offset-2",
  {
    variants: {
      variant: {
        primary:
          "bg-ink text-paper hover:bg-ink-soft active:translate-y-px",
        accent:
          "bg-accent text-paper hover:bg-accent-soft active:translate-y-px",
        ghost:
          "bg-transparent text-ink hover:bg-paper-deep border border-transparent",
        outline:
          "bg-paper-card text-ink border border-rule-strong hover:border-ink",
        link: "bg-transparent text-ink underline-offset-4 hover:underline px-0 py-0",
      },
      size: {
        sm: "h-8 px-3 text-[13px]",
        md: "h-10 px-4",
        lg: "h-12 px-6 text-[15px]",
        icon: "h-9 w-9 p-0",
      },
    },
    defaultVariants: { variant: "primary", size: "md" },
  },
);

export interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof button> {}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(function Button(
  { className, variant, size, ...rest },
  ref,
) {
  return (
    <button
      ref={ref}
      className={cn(button({ variant, size }), className)}
      {...rest}
    />
  );
});
