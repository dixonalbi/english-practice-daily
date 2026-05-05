import { VerbRepository } from "../../domain/repositories/VerbRepository";
import { VerbDTO, toVerbDTO } from "../dto/VerbDTO";
import { emptyProgress } from "@/src/shared/domain/entities/StudyProgress";

export class GetAllVerbs {
  constructor(private readonly repo: VerbRepository) {}

  execute(): VerbDTO[] {
    const all = this.repo.getAll();
    const progressMap = this.repo.getAllProgress();
    return all.map((v) => toVerbDTO(v, progressMap[v.id] ?? emptyProgress(v.id)));
  }
}
