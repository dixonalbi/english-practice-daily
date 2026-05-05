import { Verb, VerbCategory } from "../entities/Verb";
import { StudyProgress } from "@/src/shared/domain/entities/StudyProgress";

export interface VerbRepository {
  getAll(): Verb[];
  getById(id: string): Verb | null;
  getCategories(): VerbCategory[];
  getByCategory(categoryId: string): Verb[];

  getProgress(verbId: string): StudyProgress;
  getAllProgress(): Record<string, StudyProgress>;
  saveProgress(progress: StudyProgress): void;
  resetProgress(): void;
}
