"use client";

import TranscriptCard from "./TranscriptCard";
import CaptionCard from "./CaptionCard";
import { Button } from "@/components/ui/button";
import { downloadCaptions } from "@/lib/download";



type Props = {
  result: any;
};

export default function ResultsSection({ result }: Props) {
  return (
    <section className="mt-12 space-y-8">

      {/* Transcript */}
      <TranscriptCard
        transcript={result.transcript.transcript}
      />

      {/* Caption Grid */}
      <div className="grid gap-6 md:grid-cols-2">

        <CaptionCard
          title="Formal"
          emoji="💼"
          caption={result.captions.formal}
        />

        <CaptionCard
          title="Sarcastic"
          emoji="😏"
          caption={result.captions.sarcastic}
        />

        <CaptionCard
          title="Humorous Tech"
          emoji="💻"
          caption={result.captions.humorous_tech}
        />

        <CaptionCard
          title="Humorous Non-Tech"
          emoji="😂"
          caption={result.captions.humorous_non_tech}
        />

      </div>
      <div className="flex justify-center pt-4">
  <Button
    size="lg"
    onClick={() => downloadCaptions(result.captions)}
  >
    ⬇ Download All Captions
  </Button>
</div>
    </section>
  );
}