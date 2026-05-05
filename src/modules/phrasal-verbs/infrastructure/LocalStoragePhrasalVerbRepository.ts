import { PhrasalVerbRepository } from "../domain/repositories/PhrasalVerbRepository";
import { PhrasalVerb } from "../domain/entities/PhrasalVerb";
import { PHRASAL_VERBS_SEED } from "./phrasal-verbs-data";
import {
  KeyValueStore,
  sharedStorage,
} from "@/src/shared/infrastructure/storage/LocalStorageAdapter";
import {
  StudyProgress,
  emptyProgress,
} from "@/src/shared/domain/entities/StudyProgress";

const STORAGE_KEY = "phrasal-verbs:progress:v1";
type ProgressMap = Record<string, StudyProgress>;

export class LocalStoragePhrasalVerbRepository implements PhrasalVerbRepository {
  private readonly items: PhrasalVerb[];
  private readonly byId: Map<string, PhrasalVerb>;

  constructor(private readonly storage: KeyValueStore = sharedStorage) {
    this.items = PHRASAL_VERBS_SEED;
    this.byId = new Map(this.items.map((p) => [p.id, p]));
  }

  getAll(): PhrasalVerb[] {
    return this.items;
  }
  getById(id: string): PhrasalVerb | null {
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
