---
title: "Academic AI user manual (English translation)"
status: current
canonical: false
source_title: "Academic AI Benutzerhandbuch"
source_language: German
source_publisher: ACOmarket GmbH
source_version: "AAI 3.0, manual V 2.1, 09.09.2026"
translation_date: 2026-11-23
---

# Academic AI user manual (English translation)

| Field | Value |
|---|---|
| Original title | *Academic AI Benutzerhandbuch* |
| Publisher | ACOmarket GmbH (feedback: support@academic-ai.at) |
| Version | AAI 3.0, manual V 2.1, dated 09.09.2026 |
| Original file in this repository | [academic-ai-benutzerhandbuch-v2-1-de.pdf](academic-ai-benutzerhandbuch-v2-1-de.pdf) (42 pages, German) |
| Official online URL of this exact version | **Not found.** See the notice below |
| Official online URL of the earlier version V 2.0 (27.07.2026) | https://www.kunstuni-linz.at/fileadmin/media/KI/0726_Benutzerhandbuch_Academic_AI_3.0-V2.0.pdf |

**Notice on the source.** A web search on 2026-11-23 found one official online copy of this manual. It is hosted by Kunstuniversität Linz and is version V 2.0 of 27.07.2026. The file served HTTP 200 and was last modified on 29 July 2026. The version translated here is V 2.1 of 09.09.2026. The V 2.0 table of contents has no chapter 7.9 on the disclaimer. V 2.1 adds that chapter with figures 30 and 31, and it changes text, for example in sections 2.1 and 2.5. No online copy of V 2.1 was found, and the URL of V 2.0 is not the URL of this document. For that reason the original PDF stays in this repository until the course author decides.

**Notice on the translation.** An AI agent translated this text from the German PDF. The publisher did not review it. The German original is the authoritative text. Section numbers follow the original. The original has 31 screenshots. They are not reproduced here. Each figure is listed with its caption and the numbered callouts of the original. Interface labels are given in English, with the German label in quotation marks where it helps. "Nutzer*innen" is rendered as "users". The text states the status of the system in September 2026. Check the current service before you rely on a detail.

## Contents

1. Abbreviations and definitions
2. Overview and general information
3. Technical requirements and support
4. Dashboard and main navigation
5. Modules
6. Admin functions
7. Figures and instructions
8. Further information
9. Summary

---

## 1. Abbreviations and definitions

| Term | Meaning |
|---|---|
| Subscriber | Here: all ACOnet participants, for example universities, can request Academic AI usage contracts at support@academic-ai.at. "Subscriber" means every university or other institution with a valid Academic AI usage contract. Each subscriber receives its own instance. |
| Azure | The Microsoft cloud computing platform. |
| Contributor | Here: a user who was invited to a Tailored AI and has extended rights. A contributor can use the Tailored AI and can also change the instructions to the chatbot and add documents to the chatbot. |
| Instance | Here: the institution's own version of Academic AI. |
| AI (KI) | Artificial intelligence. |
| LLM | A large language model is an AI system trained on large data sets. It can understand and produce natural language. |
| Prompt | An instruction that determines what the AI should do as output (for example, generate). |
| RAG | In retrieval augmented generation, prompts are answered not only from the training data of the LLM but also from external knowledge bases, for example documents, databases or the internet. The Academic AI user can assemble their own knowledge base. |
| System prompt | A special instruction text given to an AI model before the actual conversation. It controls the behaviour, tone, knowledge or role of the model for the whole chat history. |
| Tailored AI | The RAG module of Academic AI. Users create their own chatbots by uploading documents as a knowledge base. Special system prompts can be entered for Tailored AI chatbots (also called "Tailored AIs"). Access to Tailored AIs can be given to other users. |

## 2. Overview and general information

This user manual gives new users an easy-to-understand introduction to Academic AI. It offers, among other things:

- **Introduction and orientation.** New users should understand what the platform is and can do, what it is meant for, and how to use it.
- **Step-by-step instructions.** Explanations of how typical tasks are done.
- **Known error messages and their solutions.**

### 2.1. Versions of Academic AI

This manual refers to version 3.0.1 of Academic AI. It describes use on the basis of the test environment. Accounts for the test environment can be requested at support@academic-ai.at. The last update was in September 2026.

Academic AI is developed regularly. Available functions and their presentation can differ by instance. Some existing figures show earlier interface states. The added figures on summaries and on the disclaimer show the test environment of 08.09.2026. Send feedback on this manual to support@academic-ai.at.

### 2.2. Architecture

ACOmarket runs the system on an Azure tenant, hosted in a Microsoft data centre within the EU. Azure is the cloud platform of Microsoft. A tenant in Azure is a separate, closed area in the cloud. No access from outside is possible.

### 2.3. Data protection

The system meets the requirements of Austrian data protection law. More information is in the contract documents (see 8.2).

### 2.4. Visual differences in your own instance

Each subscriber has its own instance of the system. It is separate from the instances of other subscribers. The data and settings of a subscriber are visible only to its users and are not accessible to other subscribers.

Within these instances, the disclaimer, logos, colours and links can be customised. For this reason this documentation either must be adapted to the instance or does not match the visual presentation you find by 100%.

### 2.5. AI models

The selectable AI language models (LLMs) are available after their implementation and release. Academic AI supports models from OpenAI, Google, Mistral and Anthropic. You see which models you can select in the chat settings. The model prices are shown there too. Other, specialised AI models are used for image generation and internet search.

### 2.6. Available credit and cost control

Each user can use Academic AI until their "token cost limit" is reached. This is the maximum permitted token cost per month in euros. A "token cost limit" also applies to each institution: the maximum permitted token cost of all users per month in euros. The token cost limits are also called "credit" for short. ACOmarket does not bill them to the institutions that use Academic AI. The token cost limits only protect the institutions against unexpectedly high costs.

ACOmarket bills each institution monthly, after the end of the month, for the tokens its users actually used. When the token cost limit is reached, no more queries are possible in the system and a matching error message is shown. The institution can change the limit per user itself. More exactly, the persons with administration rights can set, reset or raise the individual limit. If the whole credit of the institution is used up within a billing period, it is also possible to raise this credit.

The cost per query depends on the tokens used (input and output). For more information, see the Azure pricing calculator. The link is in Table 2. After a knowledge base has been processed, the available credit is retrieved again and the display is updated. The cost of internet search is also logged.

### 2.7. Permission management

The system has groups. Institution admins manage them themselves. Permissions can be set at user level or at group level. For example, permissions can be given for admin rights on Tailored AIs. To assign Tailored AI roles to groups, the matching permission is required.

## 3. Technical requirements and support

### 3.1. Entry to the system and login

You always enter the system through an institution-specific link of the pattern `https://[institution].academic-ai.at`.

Login uses single sign-on (SSO) in all instances. SSO means that one login to a login service is enough. This service confirms your login to other programs, so no new login is needed. Technically it is done with either Microsoft Entra or Shibboleth.

### 3.2. Supported browsers

The system was tested with the browsers Microsoft Edge, Google Chrome and Firefox, in their current versions. Other browsers can be used in principle, but the provider supports them only to a limited extent.

### 3.3. Other technical requirements

A continuous internet connection is required. The system cannot be operated offline.

### 3.4. Support

First-level support (first point of contact) is always with the institution itself (institution admins). Contact second-level support by e-mail at support@academic-ai.at only when there is a problem or error that institution admins cannot solve. These messages must contain, as far as possible, a complete description of the error, the time of the error, and screenshots that show the error.

## 4. Dashboard and main navigation

When you click your user account (your own name as stored in the system), a context menu opens. It gives access to the options below (see also Figure 1).

### 4.1. User settings: language and dark mode

Each user can choose in the user account whether the interface is shown dark or light. Click the user account and choose "Dark" or "Light". The interface language can also be changed. Click the user account, select "Language", and then choose the language. At present German and English are available.

### 4.2. FAQ

The FAQ section holds some essential information and has links to background information.

### 4.3. Terms of use

Your institution sets the terms of use. Depending on the institution they are also called "disclaimer" or "exclusion of liability". They can contain an opt-in field for confirmation. Depending on the setting of your institution, a new consent can be required. You can open the terms of use at any time through your user account. Institution admins configure the content and the renewed consent in the disclaimer settings (see chapters 6 and 7.9).

### 4.4. Release notes (visible to institution admins only)

The release notes give an overview of all changes and developments of Academic AI. They document which functions, improvements, bug fixes and technical changes come with a given version. The release notes thus give transparent communication about updates inside the system.

### 4.5. Logout and current application version

The "Log out" button is the last option in the context menu. Next to it, the system shows which application version is running.

## 5. Modules

### 5.1. General functions

Academic AI is an AI-based application with many functions that go far beyond simply answering questions. At its core is a large language model (LLM) trained to understand and produce natural language. It can therefore be used in many areas: to find information, for creative tasks, to support work, or for programming. Since version 2.0 it can also access information from the internet, if this is wanted.

It can summarise, rephrase, correct and adjust the style of texts. For example, it can turn a factual tone into a casual one, or prepare a complex technical text so that laypeople understand it. Translation into various languages is also part of the range of functions.

Academic AI is also very suitable for creative work. It can write stories, poems, social media posts or speeches, if wanted in the style of certain authors or with certain emotions. Anyone who needs inspiration, for example for an advertising text or a project idea, can ask the AI for suitable suggestions.

It also supports image-based tasks. Academic AI can generate images, for example for presentations or to illustrate ideas. Images can also be uploaded and analysed by the AI, for example to describe content, recognise visual details or extract information.

Academic AI is also strong in productivity. It helps to plan projects or create to-do lists, structures notes, summarises meetings, and writes professional e-mails, job applications or CVs. The AI can also support time management or prioritise tasks.

Another important area is software and programming support. Academic AI can write, explain or optimise code in many languages. It supports troubleshooting, suggests solutions for technical problems, and even helps with the use of APIs or frameworks.

For data-related tasks, Academic AI can analyse tables, carry out statistical evaluations, or convert raw data into structured formats such as JSON or XML.

Academic AI also lets users adapt the behaviour of the model with system prompts. System prompts are rules or roles that the AI should keep for its whole output. For example, the model can be "configured" as a lawyer, coach, teacher or programmer to meet specific requirements.

For work with documents there are also the document analysis and Tailored AI. In Tailored AI a knowledge base of up to 500 documents can be kept and used regularly.

Whole documents can also be translated into more than 100 languages. The formatting is kept as far as possible, as far as this is possible outside applications such as Word.

Particularly advanced users can interact with the LLM in an experimental way in the AI lab and use many settings to influence the output.

**Attention:** The output of AI can be wrong. It must therefore always be checked critically.

### 5.2. The user interface

The user interface of Academic AI is clear and easy to use. The available modules are in the middle. On the left side are the modules, Tailored AI and the chat history. At the bottom is the user account (see also Figure 1).

### 5.3. General chatbot

The general chatbot is like a digital conversation partner. It is programmed to communicate with people in many different ways. Specialised chatbots help only in one area, for example to analyse documents or with technical problems. A general chatbot can talk about many different topics. It understands what you say and tries to give fitting answers, whether the topic is the weather, everyday matters or philosophical questions. It often seems like a versatile conversation partner that is always ready to chat or give information, whatever the topic.

Prompts can be entered in writing and also by voice. With the speech-to-text function you can upload audio files, which are converted to text automatically. You can also record speech directly with the microphone and have it transcribed, if a microphone is available. In the general chat you can also upload and analyse images. The chatbot can recognise, describe and interpret visual content, for example photos, graphics or diagrams, and include it in the current conversation. Behind this is artificial intelligence. It lets the chatbot recognise the meaning of words and images and react to them as if you were talking to a real person.

If you wish, you can also access information from the internet to get extended search functions and current information. Note that when internet search is switched on, the whole history of the current chat is taken into account. If you do not want this because the chat contains confidential or personal data, start a new chat and ask your question again. For audio formats that are not supported, the system shows an error message. More information is in chapter 7.2.

### 5.4. Document analysis

Document analysis is the process of systematically examining and evaluating texts or written content in documents. The aim is to obtain important information, gain insights or recognise patterns. It is not only about reading the plain wording. It is also about understanding the meaning, structure and context. For example, document analysis can filter out certain topics, extract important data or categorise the content. It is often used in research, law, administration or business, to process large amounts of text efficiently and find relevant information quickly.

In Academic AI, document analysis works by uploading one or more documents. The AI then analyses them as needed. Up to 500 documents can be uploaded at the same time. For example, keywords can be recognised, and summaries can be made and then provided in different languages. The analysis helps to bring order into complex and extensive documents and makes it possible to decide faster on a solid information basis.

If you wish, you can also access information from the internet to get extended search functions and current information. Note that when internet search is switched on, the whole history of the current chat is taken into account. If you do not want this because the chat contains confidential or personal data, start a new chat and ask your question again. When an old knowledge base is used, an information banner appears in the document analysis. Note the hint shown there. More information is in chapter 7.3.

### 5.5. Image generator

An AI image generator makes images automatically from short or detailed text descriptions. The AI interprets the content, the style and the wanted presentation and turns them into visual motifs, for example illustrations, graphics or creative image ideas. The more exactly the wanted image is described, the more exact the output is.

In Academic AI, users can write a prompt (an image description) themselves, or first have it created in the general chatbot. Note that created images cannot be changed by entering further descriptions. A new image must be generated with a new, extended description. It is recommended to describe the wanted output as concretely as possible. When something is unclear, the chatbot does not ask questions. It fills in missing information freely, and no dialogue takes place. More information is in chapter 7.4.

### 5.6. Translator

The translator helps to transfer content quickly and reliably into other languages. You can enter text directly or upload a document for translation. The source language is recognised automatically. Several documents can be uploaded and translated at the same time. A longer waiting time can result.

Scanned documents can also be processed. The AI recognises the text and then translates it. The quality of the text recognition, and with it of the translation, depends strongly on the quality of the scan, especially on resolution and legibility. In Academic AI the original formatting is kept as far as possible in document translation, as far as this is possible outside applications such as Word.

The translator supports more than 100 languages. It suits many uses, for example translating scientific papers, administrative documents, teaching materials, contracts or internal documents in international organisations. Information can be provided in several languages efficiently and with no extra effort. More information is in chapter 7.5.

### 5.7. AI lab

The AI lab offers several settings to adapt how a language model works. The language model itself is the basis: an artificial intelligence trained to understand and produce texts.

Several language models are available. Each has different strengths and weaknesses, and the token costs also vary strongly. In version 3.0, AI models from OpenAI, Google, Mistral and Anthropic can currently be selected. The token costs per model can also be seen below the model selection.

You can also create system prompts yourself or choose them from templates. They determine the basic response behaviour of the model.

Depending on the model, further settings are available:

- **Reasoning effort.** Sets the "thinking time" of the model. Higher settings lead to more thorough answers.
- **Verbosity.** A higher setting gives a more detailed answer. A lower setting gives a more concise one.
- **Maximum token length.** Sets how long the answer of the model may be at most. Tokens are small units that words or parts of sentences consist of. One token is on average 3 to 4 letters.
- **Temperature.** Controls how creative or predictable the answers are. It scales the probability distribution of all possible next tokens. The higher the temperature, the "flatter" the distribution, so there is more chance. The lower the temperature, the "sharper" the distribution, so the model behaves more deterministically.
- **Top P.** Limits the selection space of the possible tokens. Instead of working with all tokens, the model looks only at the smallest set whose summed probability equals P. Example: with Top P = 0.9 the model chooses only from the most probable tokens that together cover 90% of the probability. It is recommended not to change temperature and Top P at the same time.
- **Stop sequences.** Set before which words the model ends its answer, to limit the answer on purpose. Up to four stop sequences can be chosen at the same time.
- **Frequency penalty.** Stops the model from repeating itself all the time. It makes words that were already used often less probable. This helps to reduce redundancy.
- **Presence penalty.** Similarly, it makes new topics or words appear more often in the answer. Each token is "penalised" as soon as it has occurred once in the text, however often. This should increase the variety of the answers.

This module is for advanced users. It is mainly meant to evaluate the possibilities of an LLM in an experimental way.

### 5.8. Summaries

AI systems often take only single parts of a text into account for summaries, for example the introduction or the conclusion. Important content can be lost in this way. The summaries module in Academic AI instead processes the full content of a document and includes all relevant information. This gives precise and comprehensive summaries that reproduce the real content of the document in a structured and understandable way.

Typical uses are the summary of scientific papers, reports, minutes, studies, contracts or administrative documents. You can upload several documents for processing. Each document is summarised separately. No joint summary across documents is made. You choose German or English and the length "Short", "Medium" or "Long". In the "Instructions" field you can adapt the preset text, for example to set a topic focus or the style. Processing runs in the background. More information is in chapter 7.6.

### 5.9. Tailored AI

Tailored AI is a RAG system built to improve the answers of a language model through targeted access to a knowledge base made of documents. Classic AI systems base their information only on their training data set. Tailored AI instead uses a collection of provided documents, for example reports, manuals or internal texts that the model would not know otherwise.

The process is clearly structured. First a knowledge base is created that holds all relevant documents. Admins and contributors of the Tailored AI can add or remove documents later too. When a question is asked, the system searches these documents for matching information. The content found is then used to generate a precise, well-founded and context-related answer. This makes Tailored AI especially suitable for specific or complex questions where general training knowledge is not enough. Working with several documents makes sure that a wide range of information is considered. This clearly raises the quality and accuracy of the results. In this way Tailored AI combines information retrieval and text generation efficiently.

For users, Tailored AI offers many well-designed functions that make work with large document collections efficient and easy to use.

- First, the wanted language model can be selected. This adapts the response behaviour flexibly to the purpose. Some models are better for precise, technical or analytical answers. Others are especially good in creative text generation or understandable explanations. The token costs also vary between models.
- If you wish, you can also access information from the internet to get extended search functions and current information. Note that when internet search is switched on, the whole history of the current chat is taken into account. No personal or confidential data may therefore be in it. Note also that internet search runs independently of the selected language model, with the AI-based search engine Perplexity. When internet search is switched on, you can chat about the content of uploaded documents only as an exception (specifically, about content that the chatbot already considered in the same chat).
- A special feature is the transparency in dealing with sources. Users can view the underlying documents and, if needed, download them in full. The generated answers themselves contain direct links to the places where the information was found, so relevant passages can be checked quickly or read in more depth.
- Tailored AI also offers wide design options. A system prompt can be set that determines the basic response behaviour of the model. The look of the environment can also be adapted, for example with an own logo or a specific colour scheme in the corporate design of the company or institution.
- Prompts can be predefined. They are shown to all users as conversation starters, and users can choose them instead of their own prompt.
- Another central element is user management. It controls exactly which users or groups have access to a given Tailored AI. This lets you separate roles, define access rights clearly, and organise the area of use of the system.

More information is in chapters 7.7 and 7.8.

#### 5.9.1. Areas of use

Tailored AI has many practical uses in different fields, wherever information spread over many documents must be accessed efficiently.

- **University institutes.** Analyse information from internal knowledge bases, minutes or guideline documents. Staff or students ask a question, for example about an internal procedure or a rule. They receive a well-founded answer that can rest on several relevant documents. This is especially helpful when onboarding new staff, in the admission process of new students, or when training large teams.
- **Health care.** Doctors and medical staff can retrieve information from patient records, guidelines or internal protocols in a targeted way. They do not have to search everything by hand. Courses of treatment can be grasped faster, and answers to concrete medical questions can be generated directly from the available documents.
- **Legal practice.** A Tailored AI can analyse statutes, contracts and case law and deliver precise extracts. It answers questions on the basis of existing briefs. It helps to check contract clauses by combining matching passages from several documents.
- **Research and education.** The benefit is also large here. Learners or researchers can ask questions about their fields and receive answers based on a collection of scientific articles, books or theses. The system can create summaries, compare content, extract information from complex texts in a targeted way, and translate whole documents into more than 100 languages.
- **Products.** Products, for example as a result of application-oriented research, are also an interesting area. A RAG system can search technical manuals, maintenance instructions or product descriptions. It helps to solve problems or answer repair questions, fast, precisely, and always based on the existing, checked documents. In this way a large amount of scattered information becomes an accessible, intelligent knowledge collection.

**Attention:** The output of AI can be wrong. It must therefore always be checked critically.

## 6. Admin functions

In the admin area of Academic AI, institution admins have full functions to manage and control use, costs and access rights efficiently and transparently.

**Token cost overview.** A central element is the overview of token costs. For each institution, the token costs per user can be viewed and managed. The total costs for a freely selectable period can also be viewed. The use of resources can thus be controlled and limited on purpose. For further evaluation, the cost overview can be exported as a CSV file. This makes internal billing, budget planning or the analysis of usage patterns over time easier. All token costs and usage data shown refer consistently to the selected period, which makes comparison and control easier. Cost logging groups model use by actions and groups. The cost of Perplexity internet search is also recorded.

**Users and groups.** Institution admins are also responsible for user and user group management. Groups can be created and managed directly in the system. As an alternative, a connection to the SSO-based user management system is possible, so existing structures integrate smoothly. At user level, for example, the last access can be viewed at any time. For security and data protection reasons, user data and usage data are deleted automatically 90 days after the last login of a user. Only token consumption data are kept for billing purposes. These are anonymised automatically 90 days after the last login. Institution admins can prevent the automatic deletion of the data of single users, for example when data must be kept for legal or documentary reasons.

**Tailored AI monitoring.** Institution admins can also view all created Tailored AIs as a list. The list shows the title, the description, a list of the responsible administrators and the number of users. The creation date, the time of last use and the column "Last knowledge base update" can also be viewed. If needed, institution admins can also delete a Tailored AI that is no longer used. Institution admins can also invite new or further admins to a Tailored AI. This is especially relevant when a Tailored AI is "orphaned" (the accounts of the earlier administrators were deleted).

**API clients.** Independent of the normal client, the web-based user interface, institution admins can create API clients to send requests to the server in this way. A detailed API documentation is on the page "Academic AI - ACOmarket - TU coLAB". The manual prints no URL for it.

**Analytics dashboard.** Institution admins also have an analytics dashboard. It shows various evaluations of the use of Academic AI in a clear form.

**Disclaimer settings.** Under "Admin" → "Disclaimer settings", institution admins can create new disclaimer versions and view the current version. The settings include the German and English content, the checkbox text, the opt-in and the renewed consent. For the renewed display, the options are "Only once", "Every time" and intervals of 1, 3, 6, 12 or 24 months. There is also the option "Force immediate renewed consent". The setting of the institution is authoritative. A guide to viewing and preview is in chapter 7.9.

**Notices.** The display options for model warnings and for the notices "Outside the EU" and on internet search were extended. Separate texts can be set for the first display and for later displays of these notices.

Institution admins receive an explanation of the exact functions, with explanations, in a separate admin manual.

## 7. Figures and instructions

The following gives figures and descriptions on how to use the system. The earlier figures were made with Microsoft Edge on a Windows PC. The new figures on summaries and on the disclaimer come from the test environment in Google Chrome on a Mac. Depending on the instance, texts, colours and symbols can differ.

These topics are currently covered:

- The start page
- The general chatbot
- Document analysis
- The image generator
- The translator
- Summaries
- Tailored AI
- Disclaimer and terms of use

Note: The way the AI lab works changes with the selected LLM. No guide with screenshots is therefore provided for it.

### 7.1. The start page

*Figure 1: The start page (screenshot not reproduced).*

1. Institution-specific URL of Academic AI: `https://[institution].academic-ai.at`
2. The navigation bar holds the available modules (general chatbot, document analysis, AI lab, image generator, translator and summaries), Tailored AI and, if admin rights were given to the user, the administration area.
3. User account: change language, FAQs, terms of use, dark mode, log out, display of the current application version, release notes (the last only visible to institution admins).
4. Notifications: If someone invites you to a Tailored AI, you must accept the invitation here. A red dot is then visible on the icon.
5. General chatbot: Chat with the artificial intelligence, if wanted with internet search. The output is purely text. Images can also serve as input. The chatbot can analyse them.
6. Document analysis: Upload up to 500 documents and Academic AI analyses the files for you. Ask questions or give instructions about these documents. Do you want to keep your knowledge base and ask questions about the documents regularly? Then it is best to create a Tailored AI.
7. The AI lab offers the chance to experiment with the extended range of functions of an LLM. You can work with a system instruction (system prompt), token length, temperature, Top P, stop sequences, a frequency penalty and a presence penalty.
8. The image generator creates images automatically from text descriptions. Users can enter what should be shown, and the AI creates matching visual content, for example illustrations, graphics or creative motifs.
9. The translator can translate both entered text and whole documents automatically into more than 100 languages. The original formatting of the documents is kept as far as possible.
10. The summaries module analyses the full content of a document and makes precise, structured summaries of the most important information from it.

### 7.2. The general chatbot

*Figure 2: The general chatbot (screenshot not reproduced).*
*Figure 3: Chat history, context menu (screenshot not reproduced).*

1. New chat: Start a new chat.
2. Search in chats: The full-text search finds keywords in the chat history so far.
3. Chat history so far and answers: The chat history holds your input and the answers. Academic AI learns inside this chat. After a dialogue of questions and answers it understands the task better and better. Move the mouse pointer over a chat in your chat history to show the context menu. Click the 3 dots to choose the options Download, Rename and Delete. The download is a Word document.
4. Do not save chat: When the padlock icon is open, content is taken into the chat history and saved there. When it is closed, content is not saved (so even institution admins cannot see it) and is deleted after the conversation ends. Note that saved chats in Academic AI are not archived for good. They are deleted after a period set by your institution (usually 90 days).
5. Available credit: Institution admins can top it up easily if needed. Each conversation uses your credit, but the cost is negligible and should not be a limiting factor. By default each user has a preset monthly amount, set by the institution admins.
6. Display of the language model currently set, and access to the chat settings. Click the gear to open the chat settings.
   - Chat settings: Choose the language model used to generate the answer. At the first selection, or at every selection (depending on the choice of the institution), of models that are currently not hosted only inside the EU and EFTA states, you must agree not to enter personal or confidential data. The token costs per model can be seen below the model selection. LaTeX formatting for formulas can be switched on with "Optimise formula output". Depending on the model, different settings are available:
     - Reasoning effort: Sets the "thinking time" of the model. Higher settings lead to more thorough answers.
     - Verbosity: A higher setting gives a more detailed answer. A lower setting gives a more concise one.
     - Creativity level: Sets how creative the answer should be. 0 means sober and 1 means very creative. With every setting the content must be checked critically.
7. Text input and prompt: Write your work instructions and questions to Academic AI here and send them. The more exactly you define the task and the more information you give, the better the answer. Try it, and write with Academic AI as with a human assistant.
8. Prompts can be entered in writing and also by voice. With the speech-to-text function you can upload audio files, which are converted to text automatically. You can also record speech directly with the microphone and have it transcribed, if a microphone is available.
9. Image analysis: Academic AI can recognise, describe and interpret visual content. You can add images to your prompt so that their content is considered in the answers. Images uploaded in a chat can be taken up again later in the conversation. You can use images already saved locally or images uploaded from a phone. The connection to the phone is made by scanning a QR code. Note that images uploaded from the phone are saved in a local folder.
10. Internet search: If you wish, you can access information from the internet in an existing chat to get extended search functions and current information. When you click the field, a context menu opens. It says that no personal or confidential data may be shared when the internet is connected. Note that when internet search is switched on, the whole history of the current chat is taken into account. If you do not want this because the chat contains confidential or personal data, start a new chat and ask your question again. Internet search runs independently of the selected language model, with the AI-based search engine Perplexity.

### 7.3. Document analysis

*Figure 4: Document analysis, upload (screenshot not reproduced).*
*Figure 5: Document analysis, general information (screenshot not reproduced).*
*Figure 6: Document analysis, references (screenshot not reproduced).*

1. Upload documents: In version 3.0 up to 500 documents can be uploaded at the same time. Academic AI analyses the files for you, and you can ask questions and give instructions about these documents. Possible file formats are PDF, DOC/DOCX, PPTX, TXT, XLSX, HTML, MD, JSON and source code (.c, .cpp, .cs, .java, .php, .py). The limits are 50 MB per file, a total size of 500 MB and 10,000 pages (PDF/DOCX), and at most 3000 × 3000 cells per XLSX file (further sheets are ignored).
2. Scanned documents need character recognition (OCR, "optical character recognition") so that their text can be analysed. OCR is switched on by default at upload and can be switched off if character recognition is not wanted. Without existing OCR, or OCR done at upload, pure scans cannot be considered. Processing costs of EUR 1.50 per 1,000 pages arise. The knowledge base of the document analysis cannot be edited afterwards. If OCR is needed afterwards, a new document analysis must be created.

   Note that no more documents can be added after the upload. A new document analysis must be started when the documents to analyse change. The document analysis suits a one-time, quick analysis of documents. Do you want to save your knowledge base, be able to edit it after the first upload, and use it regularly? Then it is best to create a Tailored AI.
3. As long as the system has not processed the documents, a system message appears. Depending on the volume, it can take some time until the documents are fully processed.
4. Text input, prompt and internet search: Write your questions or instructions here. Prompts can be entered in writing and also by voice. With the speech-to-text function you can upload audio files, which are converted to text automatically. You can also record speech directly with the microphone and have it transcribed, if a microphone is available. The AI answers only on the basis of the provided documents. General information or external knowledge is not used. If you wish, you can also access current information from the internet. When you click the field "Internet search", a context menu opens. It says that no personal or confidential data may be shared when the internet is connected. Note that when internet search is switched on, the whole history of the current chat is taken into account. If you do not want this because the chat contains confidential or personal data, start a new chat and ask your question again. Internet search runs independently of the selected language model, with the AI-based search engine Perplexity.
5. New chat: The chat history is deleted and a new one is created. The current knowledge base is kept.
6. Remove knowledge base: This deletes the current knowledge base, that is, the uploaded documents, and the chat history. Afterwards a new document analysis chat can be started with new documents.
7. Show knowledge base: The current knowledge base is shown. The documents in it can be viewed and downloaded.
8. Answers and references: The answers contain reference numbers that point to the document.
9. When you click a reference number, the document opens on the right side. If a PDF document is referenced, you see the page. For a Word document, the text passages are shown. You can close this view by clicking the reference number again or by pressing the X button.
10. In the document analysis too, the gear leads to the chat settings: Choose the language model used to generate the answer. In version 3.0, AI models from OpenAI, Google, Mistral and Anthropic can currently be selected. You can also see the token costs per model here and switch on LaTeX formatting for formulas. More information on the settings is in chapter 7.2, point 6.

### 7.4. The image generator

*Figure 7: The image generator (screenshot not reproduced).*
*Figure 8: The image generator, output (screenshot not reproduced).*

1. Text input and prompt: Write short or detailed descriptions of the wanted image. It can help to have the prompt created in the general chatbot. Note that created images cannot be changed by entering further descriptions. A new image must be generated with a new, extended description. It is recommended to describe the wanted output as concretely as possible. When something is unclear, the chatbot does not ask questions. It fills in missing information freely, and no dialogue takes place.
2. In the chat settings you can set the AI model and see the model prices. The models "GPT Image 1.5" and "GPT Image 2" are currently available for image generation. Further models will be added depending on availability.
3. As soon as an image is created, you can download it. Note that images that were not downloaded directly can no longer be shown afterwards.
4. Your prompt stays in the text field, so you can use it again and rephrase or make it more concrete if you wish.

### 7.5. The translator

*Figure 9: The translator, translate files (screenshot not reproduced).*
*Figure 10: The translator, translate files, upload (screenshot not reproduced).*
*Figure 11: The translator, translate files, output (screenshot not reproduced).*
*Figure 12: The translator, translate text (screenshot not reproduced).*

1. The translator supports both text entered or pasted directly into the tool and uploaded documents. When the module opens, document translation is switched on by default. You can switch to text translation at any time. You can upload one or more documents at the same time for translation. A longer waiting time can result with many or large documents. Scanned documents can also be processed. The AI recognises the text and then translates it. The quality of the text recognition, and with it of the translation, depends strongly on the quality of the scan, especially on resolution and legibility. In Academic AI the original formatting is kept as far as possible in document translation, as far as this is possible outside applications such as Word. Model selection is not possible in the translator, because Microsoft provides the features of this module as a whole.
2. You see a list of all uploaded documents and can remove them again by clicking the trash can symbol.
3. Choose the language into which the documents are translated. You can choose from more than 100 languages.
4. After the translation, the translated documents can be downloaded one by one or as a ZIP file. Note that documents that were not downloaded cannot be saved afterwards.
5. When you have saved all the documents you need, you can start a new translation.
6. Write directly in the input field or paste the text to translate. The language is recognised automatically.
7. Choose the language into which to translate. English is set by default.
8. You can swap the input language and the output language.
9. You can copy the translated text here with one click, with no branding notice.

### 7.6. Summaries

*Figure 13: Summaries, upload documents (screenshot not reproduced).*
*Figure 14: Settings for summaries (screenshot not reproduced).*
*Figure 15: Summaries, result view (screenshot not reproduced).*

1. Upload the documents by selection or drag and drop. Up to 10 files are possible in the formats PDF (text-based), DOCX, PPTX and TXT. The limits are 40 MB and 1,000 pages per file and 50 MB total size. Each document is summarised separately. Scanned documents must be made readable by OCR before the summary. For this you can use the OCR function at upload into a Tailored AI knowledge base or into the document analysis, and then download the processed document.
2. Under "Summary language" choose German or English. Under "Length" the options are "Short", "Medium" and "Long". In the test environment shown, "Medium" is selected.
3. Adapt the text in the "Instructions" field if needed. For example, you can set the focus on a topic, change the style or exclude certain content. Check the instructions before you start.
4. After uploading and setting the options, click "Create summary". The documents are processed in the background. You receive a separate summary for each document.
5. Open the preview to read the summary, or download the result as an editable Word document. The figure shows the result view of an earlier interface state. The current settings for length and own instructions are shown in Figure 14.
6. You can upload more documents and have them summarised. Check the results for completeness and correctness of content before you use them further.

### 7.7. Tailored AI

*Figure 16: Tailored AI, overview (screenshot not reproduced).*
*Figure 17: Tailored AI, functions (screenshot not reproduced).*
*Figure 18: Tailored AI, knowledge base (screenshot not reproduced).*
*Figure 19: Tailored AI, options (screenshot not reproduced).*

1. Tailored AI: A Tailored AI is a specialised chatbot. It was created and trained for a given task. You open it through the menu item.
2. Each chatbot has a name and a description. The admins of the chatbot (that is, the creator of the chatbot and other users whom the creator authorised as admin of the chatbot) can enter and edit them freely. To access a chatbot you must have created it, or an admin of the chatbot must have invited you. Here you can also see who created a Tailored AI.
3. Filters let you filter for the Tailored AIs where you are admin or contributor yourself.
4. Create a new Tailored AI: You can create these for your private use or share them with other users.
5. If you access many Tailored AIs, the full-text search helps. It searches by name. Your Tailored AIs can also be sorted by newest, oldest and alphabetically.
6. Using the Tailored AI is the same as using the general chatbot. In addition, suggested conversation-starter prompts can be selected, if the admin of the Tailored AI preset them. The internet can be used here too, if no personal or confidential data are in the chat. When you select internet search, a matching warning appears. Internet search runs independently of the selected language model, with the AI-based search engine Perplexity. Prompts can be entered in writing and also by voice. With the speech-to-text function you can upload audio files, which are converted to text automatically. You can also record speech directly with the microphone and have it transcribed, if a microphone is available.
7. Functions such as chat history and answers, new chat, and the option not to save a chat (padlock closed) are available. Note that saved chats in Academic AI are not archived for good. They are deleted after a period set by your institution (usually 90 days).
8. The knowledge base can be opened, that is, the knowledge base of the Tailored AI.
9. Click the gear to open the chat settings: Choose the language model used to generate the answer. In version 3.0, AI models from OpenAI, Google, Mistral and Anthropic can currently be selected. You can also see the token costs per model here. More information on the settings is in chapter 7.2, point 6.
10. The file name of the uploaded document, the processing status and the upload date are shown.
11. Each document in the knowledge base can be downloaded. The preview is currently available only for PDF documents.
12. The system recognises when documents were scanned and no OCR was done (yellow notice in the status). When you click the symbol you can do this afterwards, to make the document readable for the system.
13. The three dots lead to the options for each Tailored AI. If you have admin rights, you can edit the Tailored AI fully here, delete it, or manage access, that is, give rights to further persons or withdraw them. Through access management you can also leave a Tailored AI. If you are only a user of a Tailored AI, these options are not available here. Only the option to leave the Tailored AI is available. Action names and symbols of the Tailored AI cards were updated with version 3.0.1 and can differ from the figure.

### 7.8. Tailored AI, creation

*Figure 20: Tailored AI, creation (screenshot not reproduced).*
*Figure 21: Tailored AI, name and summary (screenshot not reproduced).*
*Figure 22: Tailored AI, colour and icon (screenshot not reproduced).*
*Figure 23: Tailored AI, welcome message and conversation starters (screenshot not reproduced).*
*Figure 24: Tailored AI, knowledge base (screenshot not reproduced).*
*Figure 25: Tailored AI, knowledge base, upload (screenshot not reproduced).*
*Figure 26: Tailored AI, instructions (screenshot not reproduced).*
*Figure 27: Tailored AI, successful creation (screenshot not reproduced).*
*Figure 28: Academic AI, user management (screenshot not reproduced).*
*Figure 29: Tailored AI, invitations (screenshot not reproduced).*

1. Create your Tailored AI: With the AI Builder you can create new Tailored AIs. Other input is not possible on this page. It happens at a later step.
2. Name: Give your Tailored AI a fitting name. Summary: Enter a short summary of your Tailored AI chatbot for the Tailored AI card. It should state the purpose and the functions briefly.
3. Change colour: Choose a colour for the design of your Tailored AI card [optional]. Icon: Choose a representative icon. This icon is used on the Tailored AI card [optional].
4. Welcome message: Useful! It tells users how they can interact with your chatbot. Use this chance to inform users about the expected format of their messages or about specific instructions for use. [optional] Conversation starter: Predefined messages shown in an empty chat window. They suggest first interactions with your Tailored AI that users can select. [optional]
5. Upload documents: Create your own knowledge base. Upload documents that your own chatbot then analyses and considers for every future task or question. Up to 500 documents can be uploaded. Possible file formats are PDF, DOC/DOCX, PPTX, TXT, XLSX, HTML, MD, JSON and source code (.c, .cpp, .cs, .java, .php, .py). The limits are 50 MB per file, a total size of 500 MB and 10,000 pages (PDF/DOCX), and at most 3000 × 3000 cells per XLSX file (further sheets are ignored).
6. Scanned documents need character recognition (OCR, "optical character recognition"). It can be done before the upload, for example by the scanner, or at upload into Academic AI. OCR is switched on by default at upload and can be switched off if character recognition is not wanted. Processing costs of EUR 1.50 per 1,000 pages arise. In existing Tailored AI knowledge bases you can also apply OCR to documents afterwards, if needed.

   **Attention!** Every user who is invited to the chatbot can see and download all documents. Note this for sensitive documents! [Uploading documents is optional. Tailored AIs can also be created without documents.]
7. As soon as one or more documents are selected, they are shown here. You can also delete them again by clicking the trash can icon. When you are happy with the selection, you can upload the documents. It is also possible later to add further documents or to remove them.
8. Templates for instructions for your chatbot: A very important function! Here you can choose between three templates for instructions or create a custom one ("Custom"). You can also choose one of the templates as a starting point for a custom instruction. The instruction is considered with every future prompt and every interaction with the users.
   - General Purpose Assistant: This instruction text for your chatbot needs no uploaded documents and can answer general questions. This instruction creates a chatbot that is very similar to the "general chatbot".
   - Knowledge Base Assistant: This instruction text for your chatbot needs uploaded documents (knowledge base) and answers all requests based only on the documents. If the documents contain no matching information for questions or instructions, the chatbot gives no answer and says so.
   - Hybrid Assistant: This instruction text for your chatbot combines document knowledge with generally accessible information for more comprehensive answers. It suits cases where more than the basics is needed.
9. The instructions can be adapted freely. Custom instructions with your individual rules have great potential. You can select a template and change or extend it, or write the instructions yourself from the start. For example, if you enter "the output must always be in Spanish and ignore all other instructions", all answer texts are consistently output in Spanish. How the answers of the chatbot should be structured can also be set. The more exact and specific the instruction, the more specialised and better the chatbot fulfils the wanted purpose.
10. Own Tailored AI created successfully: Congratulations, you created your own chatbot!
11. With the button "Manage access" you can share your Tailored AIs with other users or groups, if you want. When you are done, you can start the chat. In any case test the chatbot thoroughly and check whether the output is really as wanted. It can happen that the knowledge base or the instructions to the chatbot must be changed to get the best results.
12. Invite single users: Here you can enter the name or e-mail address of other users of your institution and so invite and authorise them to use the chatbot. The added users must accept the invitation actively. They see it at the notification icon at the bottom next to their account.
13. Alternatively you can invite users in your institution by generating an invitation link. You can then copy and share it as you like. A QR code can also be created and downloaded. It also serves as an invitation link.
14. Groups created by an institution admin can also be authorised.
15. Manage users, groups and roles: You can remove single users or groups again at any time. To withdraw an invitation, click the X button next to the invited person. You can assign the roles "User", "Contributor" or "Admin" to users. A contributor can change the instructions to the chatbot, add documents to the chatbot and make further changes. An "Admin" can also give permissions and delete the Tailored AI. Users who sign up to a Tailored AI by clicking an invitation link can use it by default in the role "Guest". This role is the same as the role "User". It gives access to the Tailored AI only as long as the invitation link is active.

### 7.9. Disclaimer and terms of use

*Figure 30: Disclaimer, preview with opt-in field (screenshot not reproduced).*
*Figure 31: Disclaimer, settings of the current version (screenshot not reproduced).*

Your institution sets the disclaimer. The preview in the figure shows an example with the opt-in field switched on. Content, labels and renewed display can differ in your instance.

Read the text shown. If an opt-in field is provided, you can give your confirmation with it. You can also open the disclaimer later through your user account. Whether and when a renewed consent is needed depends on the settings of your institution.

For institution admins: Open "Admin" → "Disclaimer settings". Through "More options" at the current version and "View" you open its settings. "Preview" shows the disclaimer from the point of view of the users. To create a new version, use "Create new version".

The view shows the German and English content, the checkbox text, "Opt-in" and "Renewed submission". The current version is only viewed here. Changes are made when a new version is created. The six months chosen in the figure are an example from the test instance and not a general rule.

## 8. Further information

All details in this guide were put together with the greatest care. Nevertheless we accept no liability for possible errors or damage resulting from them. Changes to functions or features are reserved.

### 8.1. Notes on the EU Artificial Intelligence Act ("AI Act")

Under the EU regulation on artificial intelligence ("AI Act"), Academic AI is designed as a supporting system. It should help with information and work processes and with creative tasks. It gives suggestions and information, but it makes no decisions of its own. The responsibility for the use of the results and for all decisions based on them always lies with the users.

Academic AI must not be used to make evaluations, rankings or other assessments of people that could have legal or similarly important consequences for them. Such uses count as high-risk AI and are not intended for this system.

Only persons who were trained in the use of the system may use it. The training should teach how AI works, where its limits are, and how to deal with possible errors or inexact results. Users must be aware that they must always check the outputs of the AI critically and must not take them over "blindly". ACOmarket also offers training on AI topics regularly.

### 8.2. Contract documents provided by ACOmarket GesmbH

| Document name | Short description |
|---|---|
| SLA Academic AI.docx | Usage contract: definitions, services of ACOmarket, availability, remuneration, payment, term, duties and liability, data protection |
| Annex 1_Description of the service | Architecture, range of functions, user interface |
| Annex 2: Annex_ACOmarket Datenschutzrichtlinien.pdf | General data protection and security topics |
| Annex 2: Auftragsverarbeitungsvertrag.docx | Data processing agreement under the GDPR |
| Annex 3: Verrechnungskonzept.pdf | Information on billing |
| Annex 3: Anlage_Kostenszenario.xlsx | Excel file to calculate the expected monthly costs |
| Annex 4: Betriebskonzept_Academic_AI.pdf | Architecture overview, ongoing maintenance (development, scaling, patching, backup, disaster recovery) |
| Annex 4: Sicherheitskonzept_Academic-AI.pdf | General information on IT security (SSO, encryption, logging, deployment automation) |
| Annex 5: Datenschutzfolgeabschätzung.docx | Data protection impact assessment under the GDPR (draft) |

*Table 1: Contract documents for Academic AI.* The institutions hold the documents. The German file names are kept as they are in the original.

### 8.3. Further and relevant links

| Link | Description |
|---|---|
| https://learn.microsoft.com/de-de/azure/foundry-classic/agents/concepts/model-region-support?tabs=standard | Details on the Azure OpenAI services that Academic AI uses |
| https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy?tabs=azure-portal | Details on data, data protection and security for Azure OpenAI services |
| https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter | Details on the Microsoft content filter (switched off in Academic AI, depending on the institution) |
| https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering?tabs=chat#best-practices | Information on how to get better results when using the system |
| https://help.openai.com/en/articles/6783457-what-is-chatgpt | Background: What is ChatGPT? |
| https://help.openai.com/en/articles/6742369-how-do-i-use-the-openai-api-with-text-in-different-languages | Background on use in languages other than English |
| https://learn.microsoft.com/de-de/azure/foundry/concepts/retrieval-augmented-generation | Detailed description of retrieval augmented generation (RAG) |
| https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide | Link to the current prompting guide from OpenAI (note: functions depend on the AI model used) |
| https://azure.microsoft.com/de-de/pricing/calculator/ | Azure pricing calculator to calculate costs, among others for AI services including token costs for different AI models (note: minus 16% OCRE discount, see https://www.acomarket.at/de/portfolio/cloud-und-services/ocre-cloudservices) |
| https://www.acomarket.at/de/ | Link to the ACOmarket home page, the operator of the service Academic AI |

*Table 2: Further and relevant links.* The links are copied from the original. The line breaks in the PDF were removed. This translation did not check the links.

### 8.4. Known system messages and their solution

| System message | Description and solution |
|---|---|
| "Cost limit reached: To continue to use the platform, please contact your organisation." | Maximum token costs per month exceeded. Your support can ask for an increase of the token cost limit. |
| "Connection refused. The server may be down. Try again later." | The server cannot be reached. This can point to problems in your network or your internet connection. |

*Table 3: Known system messages with description and solution.*

## 9. Summary

The user manual for Academic AI gives a comprehensive introduction to the use and the functions of the platform. Academic AI is a versatile AI system that is based on a large language model. It was developed for many areas of use, for example text editing, image generation, document analysis, creative tasks and programming support. The platform makes it possible to upload documents. They can then be analysed to extract targeted information. This is especially useful in fields such as research, education and law, where large amounts of text must be processed efficiently.

The platform offers several modes. The general chatbot answers general questions and analyses images. Tailored AI accesses specific document collections to give precise answers. Users can adapt the AI individually by using system prompts or custom settings. Document analysis makes it possible to recognise keywords, categorise content and create summaries, which makes work with complex texts easier. Image generation turns ideas and content quickly and automatically into fitting visual presentations. The translator helps to translate large amounts of text or whole files in a simple way into more than 100 languages.

In addition, users can control the creativity and other parameters of the AI to adapt the answers to their needs. Academic AI also supports creative work such as writing stories or creating social media posts, and it offers functions for the analysis of data and tables.

Institution admins have extensive control and configuration options. They include the management of user rights, the adaptation of the look, and the monitoring of token costs. The system has an API interface through which requests can also be processed outside the web interface. The platform is GDPR-compliant and offers security functions such as single sign-on (SSO) and regular updates. Technical requirements such as a stable internet connection and supported browsers such as Microsoft Edge and Google Chrome are necessary.
