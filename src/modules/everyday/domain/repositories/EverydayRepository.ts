import { EverydayPhrase } from "../entities/EverydayPhrase";
import { StudyProgress } from "@/src/shared/domain/entities/StudyProgress";

export interface EverydayRepository {
  getAll(): EverydayPhrase[];
  getById(id: string): EverydayPhrase | null;
  getProgress(id: string): StudyProgress;
  getAllProgress(): Record<string, StudyProgress>;
  saveProgress(p: StudyProgress): void;
  resetProgress(): void;
}
