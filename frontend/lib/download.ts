export function downloadCaptions(captions: {
  formal: string;
  sarcastic: string;
  humorous_tech: string;
  humorous_non_tech: string;
}) {
  const content = `
==============================
FORMAL
==============================

${captions.formal}

==============================
SARCASTIC
==============================

${captions.sarcastic}

==============================
HUMOROUS TECH
==============================

${captions.humorous_tech}

==============================
HUMOROUS NON-TECH
==============================

${captions.humorous_non_tech}
`;

  const blob = new Blob([content], {
    type: "text/plain;charset=utf-8",
  });

  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");
  link.href = url;
  link.download = "captions.txt";

  document.body.appendChild(link);
  link.click();

  document.body.removeChild(link);

  URL.revokeObjectURL(url);
}