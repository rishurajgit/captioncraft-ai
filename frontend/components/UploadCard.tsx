"use client";

import { Upload } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { useRef } from "react";

export default function UploadCard() {
  const inputRef = useRef<HTMLInputElement>(null);

  return (
    <div className="mx-auto max-w-3xl px-6">
      <Card className="rounded-2xl border-2 border-dashed border-violet-300 shadow-lg">
        <CardContent className="flex flex-col items-center gap-5 py-12">

          <Upload className="h-14 w-14 text-violet-600" />

          <h2 className="text-2xl font-bold">
            Upload Your Video
          </h2>

          <p className="text-center text-gray-500">
            Drag & Drop your video here
            <br />
            or click the button below.
          </p>

          <input
            type="file"
            accept="video/*"
            hidden
            ref={inputRef}
          />

          <Button
            size="lg"
            onClick={() => inputRef.current?.click()}
          >
            Choose Video
          </Button>

        </CardContent>
      </Card>
    </div>
  );
}