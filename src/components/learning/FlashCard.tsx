
import { motion, AnimatePresence } from "motion/react";
import { useState, type ReactNode } from "react";

interface Props {
  front: ReactNode;
  back: ReactNode;
  /** Resets the flip when the underlying item changes. */
  cardKey: string;
}

export function FlashCard({ front, back, cardKey }: Props) {
  const [flipped, setFlipped] = useState(false);

  function flip() {
    setFlipped((f) => !f);
  }

  function handleKey(e: React.KeyboardEvent) {
    if (e.key === " " || e.key === "Enter") {
      e.preventDefault();
      flip();
    }
  }

  return (
    <div
      className="relative w-full max-w-2xl mx-auto"
      style={{ perspective: 1600 }}
    >
      <div
        role="button"
        tabIndex={0}
        aria-label="Flip card"
        onClick={flip}
        onKeyDown={handleKey}
        className="relative cursor-pointer"
      >
        <AnimatePresence mode="wait" initial={false}>
          <motion.div
            key={`${cardKey}-${flipped ? "back" : "front"}`}
            initial={{ rotateY: flipped ? -90 : 90, opacity: 0 }}
            animate={{ rotateY: 0, opacity: 1 }}
            exit={{ rotateY: flipped ? 90 : -90, opacity: 0 }}
            transition={{ duration: 0.32, ease: [0.22, 0.61, 0.36, 1] }}
            className="bg-paper-card border border-rule rounded-sm shadow-paper p-10 md:p-14 min-h-[360px] flex flex-col justify-center"
            style={{ transformStyle: "preserve-3d", backfaceVisibility: "hidden" }}
          >
            {flipped ? back : front}
          </motion.div>
        </AnimatePresence>
      </div>
      <p className="eyebrow mt-4 text-center">
        Tap card · Space to flip
      </p>
    </div>
  );
}
