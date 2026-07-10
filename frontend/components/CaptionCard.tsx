"use client";

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

type Props = {
  title: string;
  emoji: string;
  caption: string;
};

export default function CaptionCard({
  title,
  emoji,
  caption,
}: Props) {

  async function copyCaption() {
    await navigator.clipboard.writeText(caption);
    alert("Copied!");
  }

  return (
    <Card className="h-full rounded-2xl border shadow-md transition-all hover:shadow-xl">
      <CardContent className="flex h-full flex-col justify-between p-6">

        <div>

          <h2 className="mb-4 text-xl font-bold">
            {emoji} {title}
          </h2>

          <p className="whitespace-pre-wrap leading-7 text-gray-700">
            {caption}
          </p>

        </div>

        <Button
          className="mt-6 w-full"
          onClick={copyCaption}
        >
          📋 Copy Caption
        </Button>

      </CardContent>
    </Card>
  );
}