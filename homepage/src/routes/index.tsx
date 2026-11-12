import { createFileRoute } from "@tanstack/react-router";
import hero from "@/assets/tunisia-landscape.jpg";
import date from "@/assets/date-natural.jpg";
import med from "@/assets/med-natural.jpg";
import mach from "@/assets/machine-natural.jpg";
import olive from "@/assets/olive-natural.jpg";
import aqua from "@/assets/aqua-natural.jpg";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "TNtrace — Suite nationale de traçabilité numérique" },
      { name: "description", content: "Cinq plateformes, une chaîne de confiance : dattes, olive, aquaculture, pharmacie et industrie." },
      { property: "og:title", content: "TNtrace — Suite nationale de traçabilité numérique" },
      { property: "og:description", content: "Cinq plateformes, une chaîne de confiance : dattes, olive, aquaculture, pharmacie et industrie." },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: Index,
});

function Index() {
  const media = new URLSearchParams({ hero, date, med, mach, olive, aqua });
  return <iframe src={`/tntrace.html?${media.toString()}`} title="TNtrace" className="fixed inset-0 h-screen w-screen border-0" />;
}
