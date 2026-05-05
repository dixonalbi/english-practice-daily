import { VerbRepository } from "../../domain/repositories/VerbRepository";
import { VerbDTO, toVerbDTO } from "../dto/VerbDTO";
import { VerbCategory } from "../../domain/entities/Verb";

export interface VerbCategoryGroup {
  readonly category: VerbCategory;
  readonly verbs: VerbDTO[];
}

export class GetVerbsByCategory {
  constructor(private readonly repo: VerbRepository) {}

  execute(): VerbCategoryGroup[] {
    const categories = this.repo.getCategories();
    const progressMap = this.repo.getAllProgress();

    return categories.map((category) => {
      const verbs = this.repo
        .getByCategory(category.id)
        .map((v) => toVerbDTO(v, progressMap[v.id] ?? emptyProgress(v.id)));
      return { category, verbs };
    });
  }
}

function emptyProgress(id: string) {
  return {
    itemId: id,
    masteryLevel: "NEW" as const,
    lastReviewedAt: null,
    correctStreak: 0,
    totalReviews: 0,
  };
}
