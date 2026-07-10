"use client";

import { Upload } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { useRef, useState } from "react";

import api from "@/lib/api"

import ResultSection from "@/components/ResultSection";


export default function UploadCard() {
  const inputRef = useRef<HTMLInputElement>(null);

   const [loading, setLoading] = useState(false);
   const [result, setResult] = useState<any>(null);
   async function uploadVideo(file: File) {
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await api.post(
        "/api/upload/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

    //   console.log(response.data);
    setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    }

    setLoading(false);
  }

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
            ref={inputRef}
            hidden
            type="file"
            accept="video/*"
            onChange={(e) => {
                const file = e.target.files?.[0];

        if (file) {
      uploadVideo(file);
    }
  }}
/>

          <Button
            size="lg"
            disabled={loading}
            onClick={() => inputRef.current?.click()}
          >
            {loading ? "Uploading...": "Choose Video"}
          </Button>

        </CardContent>
      </Card>

       {/* Results */}
      {result && (
  <ResultSection result={result} />
)}
    </div>
  );
}