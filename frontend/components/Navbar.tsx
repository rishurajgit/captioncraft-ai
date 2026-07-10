import { Sparkles } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="border-b bg-white">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        <div className="flex items-center gap-2">
          <Sparkles className="h-7 w-7 text-violet-600" />
          <h1 className="text-2xl font-bold tracking-tight text-violet-700">
            CaptionCraft AI
          </h1>
        </div>

        <p className="hidden text-sm text-gray-500 md:block">
          AI Powered Video Caption Generator
        </p>
      </div>
    </nav>
  );
}