"use client";

import { Card, CardContent } from "@/components/ui/card";

type Props = {
  transcript: string;
};

export default function TranscriptCard({ transcript }: Props) {
  return (
    <Card className="rounded-2xl border shadow-md">
      <CardContent className="p-6">

        <h2 className="mb-4 text-2xl font-bold">
          📄 Transcript
        </h2>

        <p className="whitespace-pre-wrap leading-8 text-gray-700">
          {transcript}
        </p>

      </CardContent>
    </Card>
  );
}