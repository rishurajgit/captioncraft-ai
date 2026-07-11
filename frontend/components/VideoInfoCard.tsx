"use client";

import { Card, CardContent } from "@/components/ui/card";

type Props = {
  filename: string;
  size: number;
  metadata: {
    duration: number;
    fps: number;
    width: number;
    height: number;
  };
};

export default function VideoInfoCard({
  filename,
  size,
  metadata,
}: Props) {
  const sizeMB = (size / (1024 * 1024)).toFixed(2);

  return (
    <Card className="rounded-2xl border shadow-md">
      <CardContent className="p-6">

        <h2 className="mb-6 text-2xl font-bold">
          🎥 Uploaded Video
        </h2>

        <div className="grid gap-4 md:grid-cols-2">

          <div>
            <p className="text-sm text-gray-500">
              Filename
            </p>

            <p className="font-semibold break-all">
              {filename}
            </p>
          </div>

          <div>
            <p className="text-sm text-gray-500">
              Size
            </p>

            <p className="font-semibold">
              {sizeMB} MB
            </p>
          </div>

          <div>
            <p className="text-sm text-gray-500">
              Duration
            </p>

            <p className="font-semibold">
              {metadata.duration.toFixed(2)} sec
            </p>
          </div>

          <div>
            <p className="text-sm text-gray-500">
              FPS
            </p>

            <p className="font-semibold">
              {metadata.fps}
            </p>
          </div>

          <div>
            <p className="text-sm text-gray-500">
              Resolution
            </p>

            <p className="font-semibold">
              {metadata.width} × {metadata.height}
            </p>
          </div>

        </div>

      </CardContent>
    </Card>
  );
}