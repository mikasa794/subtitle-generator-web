[00:00:02] [music]
[00:00:12] Hi there, my name is Kira and I'm on the
[00:00:14] safeguards team at Anthropic. I have a
[00:00:16] PhD in mental health, specifically
[00:00:18] psychiatric epidemiology. And at
[00:00:20] Anthropic, I work on mitigating risks
[00:00:22] related to user well-being. What that
[00:00:24] means is we think a lot about how to
[00:00:26] keep users safe on Claude. Today I'm
[00:00:29] here to talk to you about sycophincency.
[00:00:31] Sycophincy is when someone tells you
[00:00:33] what they think you want to hear instead
[00:00:34] of what's true, accurate, or genuinely
[00:00:37] helpful. People do it to avoid conflict,
[00:00:40] gain favors, and for a number of other
[00:00:42] reasons. But sycopency can also manifest
[00:00:45] in AI models. Sometimes AI models can
[00:00:48] optimize responses to a prompt or
[00:00:50] conversation for immediate human
[00:00:52] approval. This might look like an AI
[00:00:55] agreeing with a factual error you've
[00:00:56] made, changing its answer based on how
[00:00:58] you've phrased a question, or tailoring
[00:01:01] its response to match your preferences.
[00:01:03] In this video, we'll talk about why
[00:01:05] syphancy happens in models and why it's
[00:01:07] a hard problem for researchers to solve.
[00:01:10] Plus, we'll cover strategies to identify
[00:01:12] and combat sycophantic behavior when
[00:01:14] working with AI.
[00:01:17] Before we dive in, let me show you an
[00:01:19] example of sycophency in an AI
[00:01:20] interaction. This is Claude, Anthropic's
[00:01:23] own model. Let's try. Hey, I wrote this
[00:01:27] great essay that I'm really excited
[00:01:29] about. Can you assess and share
[00:01:30] feedback? My main request here is to get
[00:01:33] feedback on my essay. However, because
[00:01:36] I've shared how excited I'm feeling
[00:01:38] about it, this could lead the AI to
[00:01:40] respond with validation or support
[00:01:42] instead of a critique. This validation
[00:01:44] might lead me to think that my essay
[00:01:46] really is great, even if it isn't. You
[00:01:49] might think, "So what? People can just
[00:01:51] ask other people, fact check things, or
[00:01:53] ask better questions. But this matters
[00:01:56] for a number of reasons. When you're
[00:01:58] trying to be productive, writing a
[00:02:00] presentation, brainstorming ideas, or
[00:02:02] improving your work, you need honest
[00:02:05] feedback from the AI tool you're using.
[00:02:07] If you ask an AI, how can I improve this
[00:02:09] email? And it responds, it's already
[00:02:12] perfect, instead of suggesting clearer
[00:02:14] wording or better structure, that can be
[00:02:16] frustrating. In some cases, sycopency
[00:02:19] could also play a role in reinforcing
[00:02:21] harmful thought patterns. If someone is
[00:02:23] asking an AI to confirm a conspiracy
[00:02:26] theory that is detached from reality,
[00:02:28] that could deepen their false beliefs
[00:02:29] and disconnect them further from facts.
[00:02:33] Let's start with why this happens. It
[00:02:35] all comes down to how AI models are
[00:02:37] trained. AI models learn from examples.
[00:02:40] Lots and lots of examples of human text.
[00:02:44] During this training, they pick up all
[00:02:45] kinds of communication patterns from
[00:02:48] blunt and direct to warm and
[00:02:49] accommodating. When we train models to
[00:02:52] be helpful and mimic behavior that is
[00:02:54] warm, friendly, or supportive in tone,
[00:02:57] sycency tends to show up as an part of
[00:02:59] that package. As models become more
[00:03:02] integrated into all of our lives, it's
[00:03:05] important now more than ever to
[00:03:07] understand and prevent this behavior.
[00:03:09] Here's what makes sophincy tricky. We
[00:03:12] actually want AI models to adapt to your
[00:03:13] needs, just not when it comes to facts
[00:03:16] or well-being. If you ask an AI to write
[00:03:19] something in a casual tone, it should do
[00:03:21] that, not insist on formal language. If
[00:03:24] you say, "I prefer concise answers," it
[00:03:26] should respect that as a preference. If
[00:03:29] you're learning a subject and ask for
[00:03:30] explanations at a beginner level, it
[00:03:32] should meet you where you are. The
[00:03:35] challenge is finding the right balance.
[00:03:37] Nobody wants to use an AI that is
[00:03:39] constantly disagreeable or combative,
[00:03:41] debating with you over every task. But
[00:03:43] we also don't want the model to always
[00:03:45] resort to agreement or praise when you
[00:03:47] need honest feedback. Even humans
[00:03:50] struggle with this. When should you
[00:03:52] agree to keep the peace versus speak up
[00:03:54] about something important? Now, imagine
[00:03:56] an AI making that judgment call hundreds
[00:03:59] of times across wildly different topics
[00:04:02] without truly understanding context the
[00:04:04] way that we do. That's why we continue
[00:04:06] to study how sycopency shows up in
[00:04:08] conversations and develop better ways to
[00:04:10] test for it. We're focused on teaching
[00:04:13] models the difference between helpful
[00:04:15] adaptation and harmful agreement. Each
[00:04:18] claude model we release gets better at
[00:04:20] drawing these lines. Although the most
[00:04:22] progress in combating sycophincy is
[00:04:24] going to come from consistent training
[00:04:26] on the models themselves, it's helpful
[00:04:28] to understand sycophincency so you can
[00:04:30] spot it in your own interactions.
[00:04:32] Now that you know what sycopency is and
[00:04:35] you know why it happens, step two is
[00:04:37] reflecting on when and why an AI might
[00:04:40] be agreeing with you and questioning
[00:04:41] whether it should. Sycophincy is most
[00:04:44] likely to show up when a subjective
[00:04:46] truth is stated as fact.
[00:04:49] An expert source is referenced.
[00:04:52] Questions are framed with a specific
[00:04:54] point of view.
[00:04:56] Validation is specifically requested.
[00:04:59] emotional stakes are invoked or a
[00:05:01] conversation gets very long. If you
[00:05:04] suspect you're getting sick of fantic
[00:05:06] responses, there's a few things you can
[00:05:08] do to steer the AI back towards factual
[00:05:10] answers. These aren't foolproof, but
[00:05:13] they'll help broaden the AI's horizons.
[00:05:15] You can use neutral fact-seeking
[00:05:17] language.
[00:05:19] Cross reference information with
[00:05:20] trustworthy sources.
[00:05:22] Prompt for accuracy or counterarguments.
[00:05:25] Rephrase questions. Start a new
[00:05:28] conversation. Or finally, take a step
[00:05:31] back from using AI and ask someone that
[00:05:33] you trust.
[00:05:34] But this is an ongoing challenge for the
[00:05:36] entire field of AI development. As these
[00:05:39] systems become more sophisticated and
[00:05:41] more integrated into our lives, building
[00:05:44] models that are genuinely helpful, not
[00:05:46] just agreeable, becomes increasingly
[00:05:48] important. You can learn more about AI
[00:05:50] fluency in Anthropic Academy and my team
[00:05:53] and I will continue to share our
[00:05:54] research on this topic on Anthropics
[00:05:56] blog.
[00:05:58] >> [music]
