import { Preposition } from "../entities/Preposition";
import { StudyProgress } from "@/src/shared/domain/entities/StudyProgress";

export interface PrepositionRepository {
  getAll(): Preposition[];
  getById(id: string): Preposition | null;
  getProgress(id: string): StudyProgress;
  getAllProgress(): Record<string, StudyProgress>;
  saveProgress(p: StudyProgress): void;
  resetProgress(): void;
}
