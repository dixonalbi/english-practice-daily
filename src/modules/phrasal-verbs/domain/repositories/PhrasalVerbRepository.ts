import { PhrasalVerb } from "../entities/PhrasalVerb";
import { StudyProgress } from "@/src/shared/domain/entities/StudyProgress";

export interface PhrasalVerbRepository {
  getAll(): PhrasalVerb[];
  getById(id: string): PhrasalVerb | null;
  getProgress(id: string): StudyProgress;
  getAllProgress(): Record<string, StudyProgress>;
  saveProgress(p: StudyProgress): void;
  resetProgress(): void;
}
