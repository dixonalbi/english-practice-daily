import { VerbRepository } from "../domain/repositories/VerbRepository";
import { Verb, VerbCategory } from "../domain/entities/Verb";
import { loadVerbs } from "./data-loader";
import {
  KeyValueStore,
  sharedStorage,
} from "@/src/shared/infrastructure/storage/LocalStorageAdapter";
import {
  StudyProgress,
  emptyProgress,
} from "@/src/shared/domain/entities/StudyProgress";

const STORAGE_KEY = "verbs:progress:v1";

type ProgressMap = Record<string, StudyProgress>;

export class LocalStorageVerbRepository implements VerbRepository {
  private readonly verbs: Verb[];
  private readonly categories: VerbCategory[];
  private readonly byId: Map<string, Verb>;
  private readonly byCategory: Map<string, Verb[]>;

  constructor(private readonly storage: KeyValueStore = sharedStorage) {
    const loaded = loadVerbs();
    this.verbs = loaded.verbs;
    this.categories = loaded.categories;
    this.byId = new Map(this.verbs.map((v) => [v.id, v]));
    this.byCategory = new Map();
    for (const v of this.verbs) {
      const list = this.byCategory.get(v.category.id) ?? [];
      list.push(v);
      this.byCategory.set(v.category.id, list);
    }
  }

  getAll(): Verb[] {
    return this.verbs;
  }

  getById(id: string): Verb | null {
    return this.byId.get(id) ?? null;
  }

  getCategories(): VerbCategory[] {
    return this.categories;
  }

  getByCategory(categoryId: string): Verb[] {
    return this.byCategory.get(categoryId) ?? [];
  }

  getProgress(id: string): StudyProgress {
    const map = this.readMap();
    return map[id] ?? emptyProgress(id);
  }

  getAllProgress(): ProgressMap {
    return this.readMap();
  }

  saveProgress(progress: StudyProgress): void {
    const map = this.readMap();
    map[progress.itemId] = progress;
    this.storage.set(STORAGE_KEY, map);
  }

  resetProgress(): void {
    this.storage.remove(STORAGE_KEY);
  }

  private readMap(): ProgressMap {
    return this.storage.get<ProgressMap>(STORAGE_KEY) ?? {};
  }
}
