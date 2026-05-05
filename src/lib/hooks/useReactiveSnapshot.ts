
import { useCallback, useRef, useSyncExternalStore } from "react";

const listeners = new Set<() => void>();
let generation = 0;

/** Notify every snapshot subscriber that an external source changed. */
export function bumpStore(): void {
  generation += 1;
  for (const listener of listeners) listener();
}

function subscribe(cb: () => void): () => void {
  listeners.add(cb);
  return () => {
    listeners.delete(cb);
  };
}

/**
 * Reactive snapshot of an external (non-React) source. The result is cached
 * by a global generation counter — `read()` is only called once per change,
 * so referentially-fresh return values (arrays, objects) don't put React in
 * an infinite "snapshot changed" loop.
 *
 * `read` must be a stable function (defined at module scope, or memoized).
 */
export function useReactiveSnapshot<T>(read: () => T, fallback: T): T {
  const cache = useRef<{ gen: number; value: T } | null>(null);

  const getSnapshot = useCallback(() => {
    if (cache.current === null || cache.current.gen !== generation) {
      cache.current = { gen: generation, value: read() };
    }
    return cache.current.value;
  }, [read]);

  return useSyncExternalStore(subscribe, getSnapshot, () => fallback);
}
