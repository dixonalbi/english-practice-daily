/**
 * Thin wrapper around window.speechSynthesis for English pronunciation.
 * Picks a sensible en-* voice once available and exposes a single .speak().
 */
export interface SpeechService {
  speak(text: string, opts?: { rate?: number; pitch?: number }): void;
  isSupported(): boolean;
}

export class WebSpeechService implements SpeechService {
  private voice: SpeechSynthesisVoice | null = null;
  private resolved = false;

  isSupported(): boolean {
    return typeof window !== "undefined" && "speechSynthesis" in window;
  }

  private resolveVoice(): void {
    if (this.resolved || !this.isSupported()) return;
    const voices = window.speechSynthesis.getVoices();
    if (voices.length === 0) return;

    const preferred =
      voices.find((v) => /en[-_]US/i.test(v.lang) && /Samantha|Alex|Aria|Natural/i.test(v.name)) ??
      voices.find((v) => /en[-_]US/i.test(v.lang)) ??
      voices.find((v) => /en[-_]GB/i.test(v.lang)) ??
      voices.find((v) => v.lang.toLowerCase().startsWith("en")) ??
      voices[0];

    this.voice = preferred ?? null;
    this.resolved = true;
  }

  speak(text: string, opts: { rate?: number; pitch?: number } = {}): void {
    if (!this.isSupported() || !text) return;
    this.resolveVoice();

    if (!this.resolved) {
      window.speechSynthesis.onvoiceschanged = () => {
        this.resolveVoice();
        this.utter(text, opts);
      };
      return;
    }
    this.utter(text, opts);
  }

  private utter(text: string, opts: { rate?: number; pitch?: number }): void {
    const u = new SpeechSynthesisUtterance(text);
    if (this.voice) u.voice = this.voice;
    u.lang = this.voice?.lang ?? "en-US";
    u.rate = opts.rate ?? 0.95;
    u.pitch = opts.pitch ?? 1;
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(u);
  }
}

export const sharedSpeech: SpeechService = new WebSpeechService();
