import { PrepositionRepository } from "../domain/repositories/PrepositionRepository";
import { Preposition } from "../domain/entities/Preposition";
import { PREPOSITIONS_SEED } from "./prepositions-data";
import {
  KeyValueStore,
  sharedStorage,
} from "@/src/shared/infrastructure/storage/LocalStorageAdapter";
import {
  StudyProgress,
  emptyProgress,
} from "@/src/shared/domain/entities/StudyProgress";

const STORAGE_KEY = "prepositions:progress:v1";
type ProgressMap = Record<string, StudyProgress>;

export class LocalStoragePrepositionRepository implements PrepositionRepository {
  private readonly items: Preposition[];
  private readonly byId: Map<string, Preposition>;

  constructor(private readonly storage: KeyValueStore = sharedStorage) {
    this.items = PREPOSITIONS_SEED;
    this.byId = new Map(this.items.map((p) => [p.id, p]));
  }

  getAll(): Preposition[] {
    return this.items;
  }
  getById(id: string): Preposition | null {
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
