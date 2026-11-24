---
title: "Academic AI presentation, October 2026 (English translation)"
status: current
canonical: false
source_title: "Academic AI Vortrag 10/2026"
source_language: German
translation_date: 2026-11-23
---

# Academic AI presentation, October 2026 (English translation)

| Field | Value |
|---|---|
| Original title | Slide title: "Academic AI. Sicher, DSGVO- und AI-Act-konform mit Academic AI arbeiten. Ein Leitfaden für Studierende und Mitarbeiter*innen" |
| Original file in this repository | [academic-ai-vortrag-10-2026-de.pptx](academic-ai-vortrag-10-2026-de.pptx) (49 slides, German) |
| File properties | Created 2026-08-19, last saved 2026-10-23. The author field only names the tool that made the file. No publisher is stated on the slides |
| Official online URL | **Not found.** See the notice below |

**Notice on the source.** The slides say they follow the Academic AI user manual V3.0 (see the first slide). The publisher of the slide deck is not stated. Web searches on 2026-11-23 found no online copy of this deck. They found a different Academic AI deck from an event on 8 October 2026 (hosted by an event system at events.asc.ac.at), and that deck has different slides. No official URL is given here, because none could be verified. For that reason the original PPTX stays in this repository until the course author decides.

**Notice on the translation.** An AI agent translated the text of the slides from the German PPTX. Screenshots and images are not reproduced. Slides that hold only an image are marked. Speaker notes: the file has none. Most content repeats the [Academic AI user manual](academic-ai-user-manual.md). Where the slides and the manual differ, the manual is the more complete text. The slides add a few details, for example model names and the price examples on slide 11, which this translation does not check.

## Slide 1. Title

ACADEMIC AI
Work safely with Academic AI, in line with the GDPR and the AI Act
A guide for students and staff
Academic AI, user manual V3.0, academic-ai.at

## Slide 2. Overview: what to expect today

1. **Terms and rules.** The most important technical terms and rules, explained briefly.
2. **Overview and architecture.** How Academic AI is built, and why this matters for your data.
3. **Access and support.** Login, requirements, contacts.
4. **Dashboard.** The start page and basic functions.
5. **Modules in detail.** Chatbot, document analysis, image generator, translator, AI lab, summaries, Tailored AI.
6. **Admin functions.** What institution admins can control.
7. **Security, data protection and AI Act.** Why Academic AI is the right choice.
8. **Summary.** The most important points at a glance.

## Slide 3. Section 1: Terms and rules

Terms and rules, exclusion of liability
Definitions, duties and rules

## Slide 4. Terms and basics: the most important terms

- **AI (KI).** Artificial intelligence. Systems that take over human-like tasks such as understanding language.
- **LLM.** Large language model. An AI system trained on large amounts of data that understands and produces language.
- **Prompt.** Your instruction to the AI. It determines what is produced as output.
- **Azure.** The Microsoft cloud platform on which Academic AI runs.
- **Instance.** The closed version of Academic AI that belongs to your institution.
- **System prompt.** An instruction text that sets the behaviour, tone and role of the AI for the whole chat history.

## Slides 5 and 6. Terms and rules

Image-only slides. Headline: "1. Terms and rules".

## Slide 7. Section 2: Overview and architecture

How Academic AI is built

## Slide 8. Overview, architecture: your data stays in the EU, depending on the model and provider

- **Microsoft Azure.** Run by ACOmarket on its own Azure tenant.
- **Data centre in the EU.** Hosted within the EU. No data transfer to third countries is needed.
- **Closed area.** A tenant is a separate, closed cloud area. No access from outside is possible.

Additional information on the models and their training date: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai

## Slide 9. Overview, AI models: four AI providers and Perplexity to choose from

- **OpenAI.** GPT-5 and other current models.
- **Google.** Current Gemini models.
- **Mistral.** Mistral Medium 3, Mistral Large.
- **Anthropic.** Current Claude models.

Link: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai#gpt-5

## Slide 10. Overview, data protection: data protection under Austrian law

- **Austrian data protection law.** Please follow the General Data Protection Regulation. Act as the model and the provider require.
- **Data separation.** Each subscriber (each university) has its own instance, strictly separate from other institutions.
- **Visible only to your institution.** Data and settings can be seen only by users of your institution.

## Slide 11. Overview, costs: cost control with no pressure to use less

- **Token cost limit.** Each user has a personal monthly limit, set by the institution. The institution itself also has a total limit as cost protection. These limits are not billed to you. They only protect against unexpectedly high costs. Only the actual monthly consumption of the institution is billed.
- **For you in daily use.** Choose the model and the provider that fit each request best. Examples (as written on the slide): write an e-mail: Mistral, GPT 5 nano. Research: GPT 5.5, Claude, Gemini 3.1 PRO. Translation: preset. Summary: preset.

## Slide 12. Overview, costs: model prices of the AI providers

The slide holds two images (not reproduced) and this link: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai#gpt-5

## Slide 13. Overview, permissions: permission management

- **Groups.** The system has groups that institution admins manage themselves.
- **Individual or group level.** Permissions can be set per person or per group, for example admin rights on Tailored AIs.

## Slide 14. Section 3: Access and support

Technical requirements and support

## Slide 15. Access and support: how to log in

- **Institution-specific link.** Always enter through `https://[institution].academic-ai.at`.
- **Single sign-on (SSO).** Log in with your existing university account through Microsoft Entra or Shibboleth. No new password is needed.
- **Supported browsers.** Microsoft Edge, Google Chrome and Firefox in the current version.
- **Internet connection.** A continuous internet connection is required. No offline use is possible.

## Slide 16. Access and support: your way to support

1. **First-level support.** Your institution (institution admins) is always the first point of contact for questions or problems.
2. **Second-level support.** Only when institution admins cannot solve a problem: support@academic-ai.at

Tip: Describe errors as completely as possible, with the time and a screenshot.

## Slide 17. Section 4: Dashboard

The start page and main navigation

## Slide 18. Dashboard, start page: your start page at a glance

- Institution-specific URL: `https://[institution].academic-ai.at`
- Navigation bar on the left: all modules, Tailored AI and, if you have rights, the admin area.
- User account at the bottom left: language, FAQ, terms of use, dark mode, log out.
- Bell: notification, invitation to a Tailored AI.
- These modules are available, with system prompts: general chatbot, document analysis, AI lab, image generator, translator, summaries.

Caption: Figure: the start page of Academic AI.

## Slide 19. Dashboard, user account: your user account in detail

- **Language and dark mode.** Interface in German or English, light or dark.
- **FAQ.** Essential information with links to background knowledge.
- **Terms of use.** They appear once at first login and can be opened at any time.
- **Release notes.** Overview of all updates. Visible to institution admins.
- **Log out.** Also shows the application version in use.
- **Always up to date.** You can see at any time which version you work with.

## Slide 20. Dashboard, user account

Image-only slide.

## Slide 21. Dashboard, user account: links

The slide lists these links, then the line "FAQ: essential information with links to more background knowledge."

- https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai
- https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy?tabs=azure-portal
- https://learn.microsoft.com/en-us/azure/foundry-classic/foundry-models/concepts/content-filter?tabs=user-prompt
- https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering#best-practices
- https://help.openai.com/en/articles/6783457-what-is-chatgpt
- https://help.openai.com/en/articles/6742369-how-can-i-use-the-openai-api-with-text-in-different-languages

## Slide 22. Section 5: Modules in detail

The full range of functions of Academic AI

## Slide 23. 5.1 General functions: one tool for many tasks

- **Edit text.** Summarise, rephrase, correct, adjust style, translate.
- **Work creatively.** Stories, speeches, social media posts, also in the style of certain authors.
- **Create and analyse images.** Generate images, or have the AI describe uploaded images.
- **Raise productivity.** Plan projects, to-do lists, meeting summaries, e-mails, job applications.
- **Programming.** Write, explain and optimise code in many languages.
- **Evaluate data.** Analyse tables, convert raw data to JSON or XML.

## Slide 24. 5.2 General chatbot: your digital conversation partner

- Chats about any topic, from everyday questions to complex tasks.
- Prompts in writing or by voice: upload audio or speak directly into the microphone.
- Recognises and describes uploaded images (photos, graphics, diagrams).
- Selectable AI model: OpenAI, Google, Mistral or Anthropic.

Caption: Figure: the general chatbot.

## Slide 25. 5.3 General chatbot: internet search, an important data protection note

When internet search is switched on, the whole history of the current chat is taken into account. Does your chat contain confidential or personal data? Then start a new chat for the internet search and ask your question again. The search runs through the AI-based search engine Perplexity, independent of the selected language model.

- **Speech.** Speech-to-text: upload audio files or record live through the microphone.
- **Image analysis.** Add images to the prompt, also by QR code from a phone.
- **Chat history.** Academic AI learns from question-and-answer dialogues inside a chat.

## Slide 26. 5.4 Document analysis: analyse up to 500 documents at the same time

- Upload up to 500 documents at the same time (max. 50 MB per file, 500 MB in total, 10,000 pages).
- Formats: PDF, DOC/DOCX, PPTX, TXT, XLSX, HTML, MD, JSON and source code.
- OCR (text recognition) is switched on by default. Cost: EUR 1.50 per 1,000 pages.
- Answers only on the basis of your documents, optionally also with internet search.

Caption: Figure: document analysis, upload.

## Slide 27. 5.5 Document analysis: traceable answers with source references

- Answers contain reference numbers to the source document.
- A click on the number opens the passage next to the chat.
- One-time, quick analysis. For lasting knowledge bases, use Tailored AI.
- The knowledge base can be viewed and downloaded at any time.

Caption: Figure: document analysis, references.

## Slide 28. 5.6 Image generator: from text description to image

- Creates images automatically from short or detailed descriptions.
- Models: GPT Image 1.5 and GPT Image 2.
- Images cannot be adjusted afterwards. A new description gives a new image.
- The more concrete the prompt, the more exact the result. The chatbot does not ask questions when something is unclear.

Caption: Figure: the image generator, output.

## Slide 29. 5.7 Translator: translate documents into more than 100 languages

- Enter text directly or upload whole documents. The source language is recognised automatically.
- Several documents at the same time are possible, also scanned documents (quality depends on the scan).
- The original formatting is kept as far as possible.
- No model selection. The translation runs fully through Microsoft.

Caption: Figure: the translator, translate files.

## Slide 30. 5.8 Translator: also for quick text input

- Type or paste text directly. The language is recognised automatically.
- The target language can be chosen freely. Default: English.
- One click swaps the input and output language.
- Translated text can be copied without a branding notice.

Caption: Figure: the translator, translate text.

## Slide 31. 5.9 AI lab: for advanced users, more control over the model

- **Reasoning effort.** Sets the "thinking time". Higher means more thorough answers.
- **Verbosity.** A higher setting gives a more detailed answer. A lower setting gives more brevity.
- **Temperature.** Controls creativity. High means more chance. Low means more deterministic.
- **Top P.** Limits the selection space of the most probable next tokens.
- **Stop sequences.** Up to four words before which the answer ends.
- **Frequency and presence penalty.** Reduces repetitions, or raises topical variety.

Note: Language models from OpenAI, Google, Mistral and Anthropic are available. System prompts can be chosen freely or from templates.

## Slides 32 and 33. 5.10 and 5.11 AI lab

Slide 32 (label "NEW"): "Templates". Slide 33 (label "NEW"): "System prompts, models and settings can be chosen freely". Both slides are mostly images.

## Slide 34. 5.12 Summaries (new in version 3.0): precise summaries of whole documents

- Processes the full document content, not only the introduction and conclusion.
- Up to 10 documents at the same time, each document summarised separately.
- Formats: PDF (not image-based), DOCX, PPTX, TXT.
- Result as a text preview and an editable Word document.

Caption: Figure: create summaries.

## Slide 35. 5.13 Tailored AI: your own chatbot with your own knowledge base

- RAG system: answers also rest on your own documents, not only on training data.
- Ideal for reports, manuals or internal texts that the model would not know otherwise.
- Admins and contributors can extend or adapt the knowledge base at any time.
- Sources are transparent: documents can be viewed and downloaded, with direct references in the answer.

Caption: Figure: Tailored AI, overview.

## Slide 36. 5.14 Tailored AI: as flexible as the general chatbot, and more

- Free choice of the language model according to the purpose.
- Predefined conversation starters make the start easier for all users.
- A chat can be set not to save (padlock). Saved chats are deleted after about 90 days.
- Internet search is optional. Here too: no personal or confidential data.

Caption: Figure: Tailored AI, functions.

## Slide 37. 5.15 Tailored AI: knowledge base with up to 500 documents

- Formats as in document analysis: PDF, DOC/DOCX, PPTX, TXT, XLSX, HTML, MD, JSON, source code.
- OCR can be done afterwards, also for existing knowledge bases.
- **Attention:** Every invited person sees all documents and can download them.
- For sensitive documents, assign access rights with care.

Caption: Figure: Tailored AI, knowledge base.

## Slide 38. 5.16 Create a Tailored AI: your own chatbot in five steps

1. **Name and summary.** Give a fitting name and a short description for the Tailored AI card.
2. **Look (optional).** Choose a colour and an icon for the Tailored AI card.
3. **Welcome message.** Set usage hints and predefined conversation starters.
4. **Knowledge base.** Upload up to 500 documents. Optional. Use without documents is also possible.
5. **Instructions.** Choose one of three templates or write your own instructions (Custom).

## Slide 39. 5.17 Create a Tailored AI: instructions are the most important control

- General Purpose Assistant: needs no documents, similar to the general chatbot.
- Knowledge Base Assistant: answers only on the basis of your documents.
- Hybrid Assistant: combines document knowledge with general AI knowledge.
- Custom: write your own instructions freely, for example a fixed output language or structure.

Caption: Figure: Tailored AI, instructions.

## Slide 40. 5.18 Tailored AI: sharing with clearly defined roles

- User: can use the Tailored AI.
- Contributor: may also change instructions and add documents.
- Admin: may also give permissions and delete the Tailored AI.
- Invitation by name or e-mail, or by link or QR code. Whole groups are also possible.

Caption: Figure: Tailored AI, invitations.

## Slide 41. 5.9.1 Areas of use: Tailored AI in practice

- **University institutes.** Make internal knowledge bases, minutes and guidelines searchable. Ideal for onboarding.
- **Health care.** Targeted access to patient records, guidelines and internal protocols.
- **Legal practice.** Analyse statutes, contracts and case law, check clauses.
- **Research and education.** Answer questions about scientific articles, books or theses.
- **Products and support.** Search technical manuals and maintenance instructions to solve problems.
- **Always check critically.** AI output can be wrong. The responsibility stays with you.

## Slide 42. Section 6: Admin functions

What institution admins can control

## Slide 43. 6. Admin functions: full transparency and control for institutions

- **Token cost overview.** View costs per user and in total, export as CSV.
- **User management.** Manage groups, SSO connection, automatic deletion after 90 days.
- **Tailored AI monitoring.** View all Tailored AIs of the institution, take over orphaned chatbots.
- **API clients.** Create own API clients for requests outside the web interface.
- **Analytics dashboard.** Clear evaluations of the use of Academic AI.
- **Admin manual.** A separate, detailed documentation is available for institution admins.

## Slide 44. Section 7: Security, data protection and AI Act

Why Academic AI is the right choice

## Slide 45. Security and data protection: Academic AI instead of ChatGPT and others directly

Direct use of AI tools:

- It is unclear where data is stored and processed.
- Possible transfer to third countries (for example the USA).
- No institutional control over access rights.
- No cost control, no central management.

Academic AI:

- Hosting in the EU on a closed Azure tenant.
- Access by SSO. Your university stays in control.
- Data separation: one instance per institution.
- Automatic deletion periods, clear contract documents (data processing agreement under the GDPR).

## Slide 46. AI Act: Academic AI under the EU AI Act

Academic AI is designed as a supporting system. It gives suggestions and information, but it makes no decisions of its own. The responsibility for use and decisions always lies with you.

- **No use for high-risk AI.** No evaluations, rankings or assessments of people with legal or similarly important consequences.
- **Only trained users.** Training on how the system works, its limits and how to deal with errors.
- **Critical checking is a duty.** AI outputs must never be taken over "blindly". Please check every result.

## Slide 47. Data protection in detail: what happens with your data

- **90-day deletion period.** User and usage data are deleted automatically 90 days after the last login.
- **Anonymised billing data.** Only token consumption data stay for billing. They are anonymised after 90 days.
- **Contract documents.** The SLA, the data protection guidelines, the data processing agreement (AVV) and the data protection impact assessment are held by your institution.
- **No blind flight on the content filter.** The Microsoft content filter is on or off, depending on the institution. This gives transparency for your institution.

## Slide 48. Summary: the five most important points

1. **Everything in one place.** Chatbot, document analysis, image generator, translator, summaries and Tailored AI in one platform.
2. **Data protection from the start.** EU hosting, own instance per institution, clear deletion periods, data processing agreement under the GDPR.
3. **Used in line with the AI Act.** Supporting system, no high-risk uses, the responsibility stays with you.
4. **Extendable by you.** With Tailored AI, create and share your own chatbots based on your documents.
5. **Transparent costs.** Clear token cost limits protect against surprises. For you they are no limiting factor.

## Slide 49. Thank you

Thank you! Questions? We are here for you.
support@academic-ai.at (second-level support)
`[institution].academic-ai.at` (your institution-specific access)
