// "use client";

// type Props = {
//   loading: boolean;
// };

// const steps = [
//   "🎥 Uploading Video",
//   "🎤 Extracting Audio",
//   "📝 Transcribing Speech",
//   "🤖 Generating Captions",
//   "✨ Finalizing Results",
// ];

// export default function ProcessingStatus({ loading }: Props) {
//   if (!loading) return null;

//   return (
//     <div className="mx-auto mt-10 max-w-3xl rounded-2xl border bg-white p-8 shadow-lg">

//       <h2 className="mb-6 text-2xl font-bold text-center">
//         ⏳ Processing Video
//       </h2>

//       <div className="space-y-4">
//         {steps.map((step) => (
//           <div
//             key={step}
//             className="flex items-center justify-between rounded-lg border p-4"
//           >
//             <span>{step}</span>

//             <span className="animate-pulse font-semibold text-violet-600">
//               Processing...
//             </span>
//           </div>
//         ))}
//       </div>

//     </div>
//   );
// }

"use client";

import { useEffect, useState } from "react";
import { CheckCircle2, Loader2 } from "lucide-react";

type Props = {
  loading: boolean;
};

const steps = [
  "Uploading Video",
  "Extracting Audio",
  "Transcribing Speech",
  "Generating Captions",
  "Finalizing Results",
];

export default function ProcessingStatus({ loading }: Props) {
  const [currentStep, setCurrentStep] = useState(0);

  useEffect(() => {
    if (!loading) {
      setCurrentStep(0);
      return;
    }

    const interval = setInterval(() => {
      setCurrentStep((prev) => {
        if (prev < steps.length - 1) {
          return prev + 1;
        }
        return prev;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [loading]);

  if (!loading) return null;

  return (
    <div className="mx-auto mt-10 max-w-3xl rounded-2xl border bg-white p-8 shadow-lg">

      <h2 className="mb-6 text-center text-2xl font-bold">
        ⏳ Processing Video
      </h2>

      <div className="space-y-4">
        {steps.map((step, index) => (
          <div
            key={step}
            className="flex items-center justify-between rounded-xl border p-4"
          >
            <span className="font-medium">{step}</span>

            {index < currentStep ? (
              <CheckCircle2 className="h-6 w-6 text-green-600" />
            ) : index === currentStep ? (
              <Loader2 className="h-6 w-6 animate-spin text-violet-600" />
            ) : (
              <div className="h-6 w-6 rounded-full border-2 border-gray-300" />
            )}
          </div>
        ))}
      </div>
    </div>
  );
}