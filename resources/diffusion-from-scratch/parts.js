/* Manifest for this resource. base.js reads it for the parts menu, the hub
   progress bars and the weak-areas links. "sections" is the number of
   section[data-track] blocks on the page (tools/check_site.py verifies it).
   Order = recommended reading order: foundations, theory, code, upgrades, practice, reference. */
window.LR_RESOURCE = {
  id: "diffusion-from-scratch",
  title: "Diffusion from scratch",
  hub: "index.html",
  parts: [
    { id: "D0", file: "d0-start-here.html", title: "Start here: terms and Python primer", sections: 3 },
    { id: "D1", file: "d1-setup.html", title: "Phase 1: Setup", sections: 8 },
    { id: "D2", file: "d2-package-reference.html", title: "Python package reference", sections: 11 },
    { id: "D3", file: "d3-how-diffusion-works.html", title: "Phase 2: How diffusion works", sections: 20 },
    { id: "D4", file: "d4-writing-the-code.html", title: "Phase 3: Writing the code", sections: 14 },
    { id: "D5", file: "d5-making-it-good.html", title: "Phase 4: Making it good", sections: 11 },
    { id: "D7", file: "d7-interview-questions.html", title: "Interview question bank", sections: 17 },
    { id: "D8", file: "d8-practice-quiz.html", title: "Practice quiz (34 questions)", sections: 1 },
    { id: "D9", file: "d9-cheat-sheet.html", title: "Cheat sheet (printable)", sections: 1 },
    { id: "D6", file: "d6-glossary.html", title: "Full glossary, A to Z", sections: 1 },
    { id: "DX1", file: "dx1-math.html", title: "The mathematics of diffusion: DDPM derived step by step", sections: 7 },
    { id: "DX2", file: "dx2-samplers.html", title: "Samplers and speed: DDIM, ODE solvers, distillation and flow matching", sections: 9 },
    { id: "DX3", file: "dx3-latent.html", title: "Latent diffusion and how Stable Diffusion is built", sections: 7 },
    { id: "DX4", file: "dx4-control.html", title: "Fine-tuning and control: LoRA, DreamBooth, ControlNet, inpainting and editing", sections: 7 },
    { id: "DX5", file: "dx5-evaluation.html", title: "Evaluation, data, safety and ethics of image generators", sections: 6 },
    { id: "DX6", file: "dx6-beyond-images.html", title: "Beyond images: video, audio, 3D, science, robotics and discrete diffusion", sections: 9 },
    { id: "DX7", file: "dx7-training-lab.html", title: "Training lab: a tiny diffusion model, then training at scale", sections: 5 },
    { id: "DX8", file: "dx8-using-diffusers.html", title: "Using pretrained diffusion models in practice: pipelines, schedulers, memory, parameters and workflows", sections: 9 },
    { id: "DX9", file: "dx9-flows-transformers.html", title: "Flow matching, diffusion transformers and modern architectures: the exact math in one dimension", sections: 7 },
    { id: "DX10", file: "dx10-data-troubleshooting.html", title: "Data curation and troubleshooting: building image datasets and fixing common diffusion failures", sections: 10 },
    { id: "DX11", file: "dx11-intuition.html", title: "Diffusion models explained simply: analogies, pictures and plain-language answers", sections: 6 }
  ],
  topics: {
    "Setup": "d1-setup.html",
    "Forward process": "d3-how-diffusion-works.html",
    "Noise schedule": "d3-how-diffusion-works.html",
    "Training": "d3-how-diffusion-works.html",
    "U-Net": "d3-how-diffusion-works.html",
    "Sampling": "d5-making-it-good.html",
    "Guidance": "d5-making-it-good.html",
    "Practical": "d4-writing-the-code.html",
    "Diffusion math": "dx1-math.html",
    "Diffusion samplers": "dx2-samplers.html",
    "Latent diffusion": "dx3-latent.html",
    "Diffusion control": "dx4-control.html",
    "Diffusion evaluation": "dx5-evaluation.html",
    "Beyond images": "dx6-beyond-images.html",
    "Training diffusion": "dx7-training-lab.html",
    "Diffusion in practice": "dx8-using-diffusers.html",
    "Flows and transformers": "dx9-flows-transformers.html",
    "Data and troubleshooting": "dx10-data-troubleshooting.html",
    "Intuition guide": "dx11-intuition.html"
  }
};
