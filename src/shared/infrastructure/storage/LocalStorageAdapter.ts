/**
 * Generic, JSON-backed key/value adapter over window.localStorage with an
 * in-memory fallback so it can be safely instantiated server-side without
 * crashing. SSR reads return null; writes are a no-op until hydration.
 */
export interface KeyValueStore {
  get<T>(key: string): T | null;
  set<T>(key: string, value: T): void;
  remove(key: string): void;
}

export class LocalStorageAdapter implements KeyValueStore {
  private readonly memory = new Map<string, string>();

  private hasWindow(): boolean {
    return typeof window !== "undefined" && typeof window.localStorage !== "undefined";
  }

  get<T>(key: string): T | null {
    try {
      const raw = this.hasWindow()
        ? window.localStorage.getItem(key)
        : (this.memory.get(key) ?? null);
      if (raw === null) return null;
      return JSON.parse(raw) as T;
    } catch {
      return null;
    }
  }

  set<T>(key: string, value: T): void {
    const serialized = JSON.stringify(value);
    if (this.hasWindow()) {
      try {
        window.localStorage.setItem(key, serialized);
      } catch {
        this.memory.set(key, serialized);
      }
      return;
    }
    this.memory.set(key, serialized);
  }

  remove(key: string): void {
    if (this.hasWindow()) {
      window.localStorage.removeItem(key);
      return;
    }
    this.memory.delete(key);
  }
}

export const sharedStorage = new LocalStorageAdapter();
