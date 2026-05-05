import { EverydayRepository } from "../domain/repositories/EverydayRepository";
import { EverydayPhrase } from "../domain/entities/EverydayPhrase";
import { EVERYDAY_SEED } from "./everyday-data";
import {
  KeyValueStore,
  sharedStorage,
} from "@/src/shared/infrastructure/storage/LocalStorageAdapter";
import {
  StudyProgress,
  emptyProgress,
} from "@/src/shared/domain/entities/StudyProgress";

const STORAGE_KEY = "everyday:progress:v1";
type ProgressMap = Record<string, StudyProgress>;

export class LocalStorageEverydayRepository implements EverydayRepository {
  private readonly items: EverydayPhrase[];
  private readonly byId: Map<string, EverydayPhrase>;

  constructor(private readonly storage: KeyValueStore = sharedStorage) {
    this.items = EVERYDAY_SEED;
    this.byId = new Map(this.items.map((p) => [p.id, p]));
  }

  getAll(): EverydayPhrase[] {
    return this.items;
  }
  getById(id: string): EverydayPhrase | null {
    return this.byId.get(id) ?? null;
  }
  getProgress(id: string): StudyProgress {
    return this.read()[id] ?? emptyProgress(id);
  }
  getAllProgress(): ProgressMap {
    return this.read();
  }
  saveProgress(p: StudyProgress): void {
    const map = this.read();
    map[p.itemId] = p;
    this.storage.set(STORAGE_KEY, map);
  }
  resetProgress(): void {
    this.storage.remove(STORAGE_KEY);
  }
  private read(): ProgressMap {
    return this.storage.get<ProgressMap>(STORAGE_KEY) ?? {};
  }
}
