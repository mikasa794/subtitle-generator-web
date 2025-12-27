[00:00:00] do lead work on Codex.
[00:00:01] >> Codex is Open's coding agent. We think
[00:00:03] of Codex as just the [music] beginning
[00:00:05] of a software engineering teammate. It's
[00:00:06] a bit like this really smart intern that
[00:00:09] refuses to read Slack, doesn't check
[00:00:11] Data [music] Dog unless you ask it to.
[00:00:12] >> I remember Carpot that he tweeted the
[00:00:14] gnarliest bugs that he runs into that he
[00:00:16] just spends hours trying to figure out.
[00:00:18] Nothing else has solved. He gives it to
[00:00:19] Codex, lets it run for an hour and it
[00:00:21] solves it.
[00:00:21] >> Starting to see glimpses of the future
[00:00:22] where we're actually starting to have
[00:00:24] Codeex be on call for its own training.
[00:00:26] Codex writes a lot of the code that
[00:00:27] helps like manage its training run. the
[00:00:29] key infrastructure. [music] And so we
[00:00:30] have a codeex code review is like
[00:00:32] catching a lot of mistakes. It's
[00:00:33] actually caught some like pretty
[00:00:34] interesting configuration mistakes. One
[00:00:36] of the most mind-blowing examples of
[00:00:37] acceleration, the Sora Android app, like
[00:00:39] a fully new app. We built it in 18 days
[00:00:42] and then 10 days later, so 28 days
[00:00:44] total, we went to the public.
[00:00:45] >> How do you think you win [music] in this
[00:00:47] space?
[00:00:47] >> One of our major goals with Codex is to
[00:00:49] get to proactivity. If we're going to
[00:00:50] build a super assistant has to be able
[00:00:51] [music] to do things. One of the
[00:00:52] learnings over the past year is that for
[00:00:54] models to do stuff, they are much more
[00:00:55] effective when they can use a computer.
[00:00:57] It turns out the best way for models to
[00:00:58] use [music] computers is simply to write
[00:01:00] code. And so we're kind of getting to
[00:01:01] this idea where if you want to build any
[00:01:02] agent, maybe you should be building a
[00:01:04] coding agent.
[00:01:04] >> When you think about progress on codecs,
[00:01:07] I imagine you have a bunch of evals and
[00:01:08] there's all these public benchmarks.
[00:01:10] >> A few of us are like constantly on
[00:01:11] Reddit. You know, there's a there's
[00:01:13] praise up there and there's a lot of
[00:01:14] complaints. What we can do as a product
[00:01:16] team just [music] try to always think
[00:01:17] about how are we building a tool so that
[00:01:18] it feels like we're maximally
[00:01:20] accelerating people rather than building
[00:01:21] a tool that makes it more unclear what
[00:01:23] you should do as the human. Being at
[00:01:24] OpenAI, I can't not ask about how far
[00:01:26] you think we are from AGI.
[00:01:28] >> The current underappreciated [music]
[00:01:29] limiting factor is literally human
[00:01:30] typing speed or human multitasking
[00:01:32] speed.
[00:01:35] Today, my guest is Alexander Emiros,
[00:01:37] product lead for Codeex, OpenAI's
[00:01:39] incredibly popular and powerful coding
[00:01:41] agent. In the words of Nick Turley, head
[00:01:44] of Chachi BT and former podcast guest,
[00:01:46] Alex is one of my all-time favorite
[00:01:48] humans I've ever worked with, and
[00:01:49] bringing him and his company into OpenAI
[00:01:51] ended up being one of the best decisions
[00:01:53] we've ever made. Similarly, Kevin Wheel,
[00:01:56] OpenAI CPO, said, "Alex is simply the
[00:01:58] best." In our conversation, we chat
[00:02:00] about what it's truly like to build
[00:02:02] product at OpenAI. How Codeex allowed
[00:02:04] the Sora team to ship the Sora app,
[00:02:06] which became the number one app in the
[00:02:07] app store in under one month. Also, the
[00:02:10] 20x growth Codex is seeing right now and
[00:02:12] what they did to make it so good at
[00:02:14] coding. Why his team is now focused on
[00:02:16] making it easier to review code, not
[00:02:18] just write code. His AGI timelines, his
[00:02:20] thoughts on when AI agents will actually
[00:02:22] be really useful, and so much more. A
[00:02:25] huge thank you to Ed Baze, Nick Turley,
[00:02:27] and Dennis Yang for suggesting topics
[00:02:28] for this conversation. If you enjoy this
[00:02:30] podcast, don't forget to subscribe and
[00:02:32] follow it in your favorite podcasting
[00:02:33] app or YouTube. And if you become an
[00:02:35] annual subscriber of my newsletter, you
[00:02:38] get a year free of 19 incredible
[00:02:40] products, including a year free of
[00:02:43] Devon, Lovable, Replet, Bolt, Nadam,
[00:02:45] Linear, Superhum, Descript, Whisper
[00:02:46] Flow, Gamma, Perplexity, Warp, Granola,
[00:02:48] Magic Patterns, Raycast, Champardd, Mob
[00:02:49] and Post Hog, and Stripe Atlas. Head on
[00:02:52] over to lenniesnewsletter.com and click
[00:02:54] product pass. With that, I bring you
[00:02:56] Alexander and Biricos after a short word
[00:02:58] from our sponsors.
[00:03:00] Here's a puzzle for you. What do OpenAI,
[00:03:02] Cursor, Perplexity, Verscell, Platt, and
[00:03:05] hundreds of other winning companies have
[00:03:07] in common? The answer is they're all
[00:03:09] powered by today's sponsor, Work OS. If
[00:03:12] you're building software for
[00:03:13] enterprises, you've probably felt the
[00:03:14] pain of integrating single signon, skim,
[00:03:17] arbback, audit logs, and other features
[00:03:20] required by big customers. Work OS turns
[00:03:22] those deal blockers into drop-in APIs
[00:03:25] with a modern developer platform built
[00:03:27] specifically for B2B SAS. Whether you're
[00:03:29] a seedstage startup trying to land your
[00:03:31] first enterprise customer or a unicorn
[00:03:33] expanding globally, work OS is the
[00:03:35] [music] fastest path to becoming
[00:03:36] enterprise ready and unlocking growth.
[00:03:39] They're essentially Stripe for
[00:03:40] enterprise features. Visit workos.com to
[00:03:43] get started or just hit up their Slack
[00:03:45] support where they have real engineers
[00:03:46] in there who answer your questions super
[00:03:48] fast. Workos allows you to build like
[00:03:51] the best with delightful APIs,
[00:03:53] comprehensive docs, and a smooth
[00:03:55] developer experience. Go to works.com to
[00:03:58] make your app enterprise ready today.
[00:04:01] This episode is brought to you by Finn,
[00:04:03] the number one AI agent for customer
[00:04:05] service. If your customer support
[00:04:07] tickets are piling up, then you need
[00:04:08] Finn. Finn is the highest performing AI
[00:04:11] agent on the market with a 65% average
[00:04:14] resolution rate. Finn resolves even the
[00:04:16] most complex customer queries. No other
[00:04:18] AI agent performs better. In
[00:04:20] head-to-head bake offs with competitors,
[00:04:22] Finn wins every time. Yes, switching to
[00:04:25] a new tool can be scary, but Finn works
[00:04:27] on any help desk with no migration
[00:04:29] needed, which means you don't have to
[00:04:30] overhaul your current system or deal
[00:04:32] with delays in service for your
[00:04:34] customers. [music] And Finn is trusted
[00:04:35] by over 6,000 customer service leaders
[00:04:37] and top companies like Anthropic,
[00:04:39] Shuttertock, Cynthia, Clay, Vant,
[00:04:41] Lovable,Mundday.com, and more. And
[00:04:43] because Finn is powered by the Finn AI
[00:04:45] engine, which is a continuously
[00:04:47] improving system that allows you to
[00:04:48] analyze, train, test, and deploy with
[00:04:50] ease, Finn can continuously improve your
[00:04:53] results, too. So, if you're ready to
[00:04:54] transform your customer service, and
[00:04:56] scale your support, give Finn a try for
[00:04:58] only 99 cents per resolution. Plus, Finn
[00:05:01] comes with a 90-day money back
[00:05:02] guarantee. Find out how Finn can work
[00:05:04] for your team at f.ai/lenny.
[00:05:08] That's finn.ai/lenny.
[00:05:14] Alexander, thank you so much for being
[00:05:16] here and welcome to the podcast.
[00:05:18] >> Thank you so much. I've been following
[00:05:19] for ages and I'm excited to be here.
[00:05:21] >> I'm even more excited. I really
[00:05:22] appreciate that. I want to start with
[00:05:24] your time at Open AI. So, you joined
[00:05:27] OpenAI about a year ago. Before that,
[00:05:30] you had your own startup for about 5
[00:05:32] years. Before that, you were a product
[00:05:34] manager at Dropbox. I imagine OpenAI is
[00:05:37] very different from every other place
[00:05:39] you've worked. Let me just ask you this.
[00:05:41] What is most different about how OpenAI
[00:05:44] operates? And what's something that
[00:05:45] you've learned there that you think
[00:05:46] you're going to take with you wherever
[00:05:48] you go, assuming you ever leave? By far,
[00:05:50] I would say the speed and ambition of
[00:05:53] working at OpenAI are just like
[00:05:54] dramatically more than what I can
[00:05:56] imagine. And you know, I guess it's kind
[00:05:58] of an embarrassing thing to say because
[00:05:59] you, you know, everyone who's a startup
[00:06:01] founder thinks like, "Oh yeah, my
[00:06:02] startup moves super fast and the talent
[00:06:04] bar is super high and we're super
[00:06:05] ambitious." But I have to say like
[00:06:07] working at OpenAI just kind of like made
[00:06:08] me reimagine what he what that even
[00:06:10] means. We hear this a lot about, you
[00:06:12] know, feels like every AI company is
[00:06:14] just like, "Oh my god, I can't believe
[00:06:15] how fast they're moving." Is there an
[00:06:17] example of just like, "Wow, that
[00:06:18] wouldn't have happened this quickly
[00:06:19] anywhere else."
[00:06:20] >> The most obvious thing that comes to
[00:06:21] mind is just like the the explosive
[00:06:23] growth of codeex itself. I think it's a
[00:06:26] while since we bumped our external
[00:06:27] number, but like you know it's like the
[00:06:29] the 10xing of Codeex's scale was just
[00:06:32] like super fast in a matter of months
[00:06:34] and it's like well more since then and
[00:06:37] you know like once you've lived through
[00:06:38] that or at least speaking for myself
[00:06:40] like having lived through that now I
[00:06:42] feel like anytime I'm going to spend my
[00:06:45] time on like you know building tech
[00:06:47] product there's that kind of that speed
[00:06:49] and scale that I now need to to to meet.
[00:06:52] If I think of like what I was doing in
[00:06:54] my startup, it moved like way slower.
[00:06:56] And I, you know, there's always this
[00:06:58] balance with startups of like how much
[00:07:00] do you commit to an idea that you have
[00:07:01] versus like find out that it's not
[00:07:03] working uh and then pivot. But I think
[00:07:06] one thing I've realized at OpenAI is
[00:07:07] like the the amount of impact that we
[00:07:09] can have and in fact need to have to do
[00:07:11] a good job is so high that it it's I
[00:07:13] have to be like way more ruthless with
[00:07:14] how I spend my time. Before we get to
[00:07:16] codeex, is there a way that they've
[00:07:18] structured the org or I don't know the
[00:07:20] way that open operates that allows the
[00:07:22] team to move this quickly because
[00:07:23] everyone everyone wants to move super
[00:07:25] fast. I imagine there's a structural
[00:07:27] approach to allowing this to happen.
[00:07:29] >> I mean, so one thing is just the
[00:07:30] technology that we're building with has
[00:07:33] like just transformed so many things,
[00:07:35] you know, from like both how we build
[00:07:37] but also like what kinds of things we
[00:07:39] can enable uh for users. And you know we
[00:07:42] spend most of our time talking about
[00:07:43] like the sort of improvements within the
[00:07:46] foundation models but I I believe that
[00:07:47] even if we had no more progress today
[00:07:49] with models which is absolutely not the
[00:07:51] case but if even if we had no more
[00:07:52] progress we are way behind on product.
[00:07:55] There's so much more product to build.
[00:07:56] >> So I think like just like the moment is
[00:07:59] ripe if that makes sense.
[00:08:01] >> But I think there's a lot of sort of
[00:08:02] counterintuitive things that surprised
[00:08:04] me when I arrived as far as like how
[00:08:06] things are structured. One example that
[00:08:08] comes to mind is like when I was working
[00:08:10] on my startup and and before that when I
[00:08:11] was a dropbox, it was like very
[00:08:12] important, you know, especially as a PM
[00:08:14] to like always kind of rally the ship
[00:08:16] and it was kind of like make sure you're
[00:08:17] pointed in the right direction and that
[00:08:18] you can like accelerate in that
[00:08:19] direction. But here I think because we
[00:08:24] don't exactly know like what
[00:08:25] capabilities will even come up soon and
[00:08:27] we don't know what's going to work uh
[00:08:29] technically and then we also don't know
[00:08:31] what's going to land even if it works
[00:08:33] technically. It's much more important
[00:08:34] for us to be very like humble and learn
[00:08:38] a lot more empirically and just try
[00:08:39] things quickly and like the org is is
[00:08:42] set up in that way to to be incredibly
[00:08:44] bottoms up. You know, this is again one
[00:08:46] of those things that like as you were
[00:08:47] saying, everyone wants to move fast. I
[00:08:48] think everyone likes to say that they're
[00:08:50] bottoms up or at least a lot of people
[00:08:51] do, but OpenAI is like truly truly
[00:08:53] bottoms up and that's like been a
[00:08:55] learning experience for me that now like
[00:08:58] it it'll be interesting if I ever work
[00:09:00] at like I don't think it'll ever it'll
[00:09:02] even make sense to work at a nonAI
[00:09:04] company in the future. I don't even know
[00:09:05] what that means. But if I were to
[00:09:07] imagine it or go back in time, I think I
[00:09:08] would like run things totally different.
[00:09:10] >> What I'm hearing is kind of this uh
[00:09:12] ready, fire, aim uh is the approach more
[00:09:15] than ready, aim, fire. And this
[00:09:17] something and as you processed that uh
[00:09:20] because that may not come across well
[00:09:21] but I actually have heard this a lot at
[00:09:23] AI companies is because you don't know
[00:09:25] and Nick Charlie shared I think the same
[00:09:27] sentiment because you don't know how
[00:09:28] people will use it. It doesn't make
[00:09:30] sense to spend a lot of time making it
[00:09:31] perfect. It's better to just get it out
[00:09:34] there in a primordial way see how people
[00:09:36] use it and then go big on that use case.
[00:09:39] Yeah. It's like to okay to use this
[00:09:41] analogy a little bit I feel like there
[00:09:42] there is an aim component but the aim
[00:09:44] component is much fuzzier. you know,
[00:09:46] it's kind of like roughly what do we
[00:09:48] think can happen? like someone um I've
[00:09:50] learned a ton from working here is a is
[00:09:52] a research lead and he likes to say that
[00:09:54] like in open AI we can can have really
[00:09:57] good conversations about something
[00:09:58] that's like a year plus from now and you
[00:10:01] know there's a lot of ambiguity in what
[00:10:02] will happen but but like that's a right
[00:10:04] sort of timeline and then we can have
[00:10:05] really good conversations about what's
[00:10:07] happening like in like low months or low
[00:10:09] or weeks but there's kind of this like
[00:10:11] awkward middle ground which was like as
[00:10:13] you start approaching a year but you're
[00:10:14] not at a year where it's like very
[00:10:16] difficult to reason about right and so
[00:10:18] as far As far as like aiming, I think we
[00:10:19] want to know like, okay, what are some
[00:10:21] of the futures that we're trying to
[00:10:22] build towards and like a lot of the
[00:10:24] problems we're dealing with in AI, like
[00:10:25] such as alignment, are problems you need
[00:10:26] to be thinking out like really far out
[00:10:28] into the future. So, we're kind of
[00:10:30] aiming fuzzily there. But when it comes
[00:10:32] down to the more tactically like, oh
[00:10:34] yeah, like what product will we build
[00:10:35] and therefore how will people use that
[00:10:37] product? That's the place where we're
[00:10:39] much more like let's find out
[00:10:40] empirically.
[00:10:41] >> That's a good way of putting it.
[00:10:42] Something else that when people hear
[00:10:44] this, they people sometimes hear
[00:10:47] companies like yours saying, "Okay,
[00:10:49] we're gonna be bottoms up. We're gonna
[00:10:50] try a bunch of stuff. We're not going to
[00:10:51] have exactly a plan of where it's going
[00:10:53] in the next few months." The key is you
[00:10:55] all hire the best people in the world.
[00:10:57] And so that feels like a really key
[00:10:59] ingredient in order to be this
[00:11:00] successful at Bottoms Upwork. it just
[00:11:02] super resonates basically.
[00:11:04] >> Um I was just like again surprised or
[00:11:07] even shocked when I arrived at like the
[00:11:09] level of like individual like drive and
[00:11:11] like autonomy that everyone here has. So
[00:11:15] I think like the way that OpenAI runs
[00:11:18] like many you can't like read this or be
[00:11:20] on listen to a podcast and be like I am
[00:11:22] I'm just going to deploy this to my
[00:11:23] company. Um you know maybe this is a
[00:11:26] harsh thing to say but I think like yeah
[00:11:27] very few companies have the talent
[00:11:28] caliber to be able to do that. So it
[00:11:31] might need to be like adjusted if you
[00:11:33] were going to implement this.
[00:11:34] >> Okay. So let's talk codeex. You lead
[00:11:36] work on codeex. How's codeex going? What
[00:11:39] numbers can you share? Is there anything
[00:11:40] you can share there? Also just not
[00:11:42] everyone knows exactly what codeex is.
[00:11:43] Explain what codeex is. Totally. Yeah.
[00:11:46] So uh I have the very lucky job of of
[00:11:48] living in the future and leading
[00:11:49] products on codeex. Um and codeex is
[00:11:53] open coding agent. So super concretely
[00:11:56] that means it's an IDE extension VS code
[00:11:59] extension uh that you can install or a
[00:12:01] terminal tool that you can install and
[00:12:02] when you do so you can then basically
[00:12:05] pair with codeex to answer questions
[00:12:06] about code write code uh you know run
[00:12:09] tests execute code and do a bunch of the
[00:12:12] work in sort of that like thick middle
[00:12:14] section of the software development life
[00:12:15] cycle which is all about uh you know
[00:12:18] writing code that you're going to get
[00:12:19] into production. Uh more broadly we
[00:12:22] think of codeex as like it's the what it
[00:12:25] currently is is just the beginning of a
[00:12:27] software engineering teammate. And so
[00:12:29] you know when we when you when we use a
[00:12:30] big word like teammate like some of the
[00:12:32] things we're imagining are that it's not
[00:12:34] only able to to write code but actually
[00:12:36] it participates like early on in like
[00:12:38] the ideation and planning phases of
[00:12:40] writing software and then further
[00:12:41] downstream in terms of like validation
[00:12:43] deploying and like maintaining code. to
[00:12:46] make that a little more fun. Like one
[00:12:48] thing I like to imagine is like if you
[00:12:49] think of what Codex is today, it's a bit
[00:12:51] like this like really smart intern that
[00:12:53] like refuses to read Slack and like
[00:12:55] doesn't check data dog or like Sentry
[00:12:57] unless you ask it to. And so like no
[00:12:59] matter how smart it is, like how much
[00:13:00] are you going to trust it to write code
[00:13:02] without you also working with it, right?
[00:13:03] So that's how people use it mostly today
[00:13:05] is they pair with it.
[00:13:06] >> But we want to get to the point where
[00:13:08] you know it can work like just like a
[00:13:10] new intern that you hire, you don't only
[00:13:12] ask them to write code, but you ask them
[00:13:13] to participate across the cycle. And so
[00:13:15] you know that like even if they don't
[00:13:16] get something right the first try,
[00:13:17] they're eventually going to be able to
[00:13:18] iterate their way there.
[00:13:20] >> I thought the way uh I thought the point
[00:13:21] about not reading Slack in Dave Dog was
[00:13:23] it's just not distracted. It's just
[00:13:24] constantly focused and is always in
[00:13:26] flow. But I get what you're saying there
[00:13:28] is it doesn't have all the context on
[00:13:30] everything that's going on.
[00:13:31] >> And like that's not only true when it's
[00:13:33] performing a task, but again if you
[00:13:34] think of like the best human teammates,
[00:13:36] like you don't tell them what to do,
[00:13:37] >> right? Like maybe when you first hire
[00:13:39] them, you have like a couple meetings
[00:13:40] and you're like, "Hey, like you kind of
[00:13:42] learn like, okay, this is this these
[00:13:44] prompts work for this teammate. These
[00:13:45] prompts don't, right? This is how to
[00:13:46] communicate with this person." Then
[00:13:48] eventually you give them some starter
[00:13:49] tasks. You delegate a few tasks. But
[00:13:50] then eventually you just say like, "Hey,
[00:13:51] great. Okay, you're working with this
[00:13:53] set of people in this area of the
[00:13:55] codebase. You know, feel free to work
[00:13:57] with other people in other parts of the
[00:13:58] codebase too even." And yeah, you tell
[00:14:00] me what you think makes sense to be
[00:14:01] done, right? And so, you know, we think
[00:14:03] of this as like proactivity and like one
[00:14:05] of our major goals with Codeex is to
[00:14:06] like get to proactivity.
[00:14:09] I think this is this is like critically
[00:14:12] important to like achieve the mission of
[00:14:13] OpenAI which is to deliver the benefits
[00:14:15] of AI to all humanity. You know, I like
[00:14:17] to joke today that like AI products and
[00:14:19] it's it's a half joke. They're actually
[00:14:21] like really hard to use because you have
[00:14:23] to like be very thoughtful about when it
[00:14:27] could help you. And if you're not
[00:14:29] prompting a model to help you, it's
[00:14:31] probably not helping you at that time.
[00:14:33] And if you think of how many times like
[00:14:34] the average user is prompting AI today,
[00:14:36] it's probably like tens of times. But if
[00:14:38] you think of how many times people could
[00:14:40] actually get benefit from a really
[00:14:42] intelligent entity, it's thousands of
[00:14:44] times per day. And so a large a large
[00:14:46] part of our our goal with codeex is to
[00:14:48] figure out like what is the shape of an
[00:14:50] actual teammate agent that is sort of
[00:14:52] helpful by default. When people think
[00:14:54] about cursor and uh even cloud code, it
[00:14:57] it's like a IDE that helps you code and
[00:14:59] kind of autocompletes code and maybe
[00:15:01] does some agentic work. What I'm hearing
[00:15:03] here is the vision is is different which
[00:15:05] is it's a teammate. It's like a remote
[00:15:07] teammate, a building code for you that
[00:15:09] you talk to and ask to do things and it
[00:15:12] also does IDE autocomplete and things
[00:15:14] like that. Is that is that a kind of a
[00:15:16] differentiator in the way you think
[00:15:17] about codecs? It's basically this idea
[00:15:19] that like we want the way like if you're
[00:15:22] a developer and you're trying to get
[00:15:24] something done, we want you to just feel
[00:15:25] like you have superpowers and you're
[00:15:27] able to move much much faster. But we
[00:15:29] don't think that in order for you to
[00:15:31] reap those benefits, you need to be
[00:15:33] sitting there constantly thinking about
[00:15:35] like how can I invoke AI at this point
[00:15:37] to do this thing. We want you to be able
[00:15:38] to sort of like plug it in to the way
[00:15:40] that you work and have it just start to
[00:15:42] do stuff without you having to think
[00:15:43] about it.
[00:15:43] >> Okay. I have a lot of questions along
[00:15:44] those lines, but uh just how's it going?
[00:15:46] Is there any stats, any numbers you can
[00:15:48] share about how Codex is doing?
[00:15:49] >> Yeah, it's been Codex has been growing
[00:15:51] like absolutely explosively um since the
[00:15:53] launch of GPT5 back in August. Um
[00:15:55] there's some definitely some interesting
[00:15:57] like product insights to talk about as
[00:15:58] to like how we unlock that growth if
[00:16:00] you're interested. But yeah, the last
[00:16:02] the last stat we shared there was like
[00:16:03] we we were like well over 10x since
[00:16:06] August. In fact, it's been like 20x
[00:16:08] since then. Um, also the codex models
[00:16:10] are serving many many trillions of
[00:16:12] tokens a week now and it's basically
[00:16:14] like our most served coding model. Um,
[00:16:17] one of the really cool things that we've
[00:16:18] seen is that the way that we decided to
[00:16:20] set up the codeex team uh was to build a
[00:16:23] you know really tightly integrated
[00:16:25] product and research team that are
[00:16:27] iterating on the model and the harness
[00:16:28] together. And it turns out that lets you
[00:16:30] just do a lot more and try many more
[00:16:32] experiments as to how these things will
[00:16:34] work together. And so we were just
[00:16:36] training these models for use in our
[00:16:38] first party harness that we were very
[00:16:40] opinionated about. And then what we've
[00:16:42] started to see more recently actually is
[00:16:44] that other major sort of API coding
[00:16:47] customers are now starting to adopt
[00:16:48] these models as well. And so we've
[00:16:50] reached a point where actually the
[00:16:51] codeex model is the most served coding
[00:16:53] model in the API as well.
[00:16:55] >> You uh hinted at this uh what unlocked
[00:16:59] this growth? I am extremely interested
[00:17:00] in hearing that. It felt like before, I
[00:17:03] don't know, maybe this was before you
[00:17:04] joined the team. It just felt like cloud
[00:17:05] code was killing it. Just everyone was
[00:17:07] sitting on top of cloud code. It was by
[00:17:10] far the best way to code. And then all
[00:17:11] of a sudden, Codex comes around. I
[00:17:13] remember Carpathy tweeted that he just
[00:17:16] like has never seen a model like this.
[00:17:18] He I think the tweet was the gnarliest
[00:17:20] bugs that he runs into that he just
[00:17:22] spends hours trying to figure out.
[00:17:23] Nothing else has solved. He gives it to
[00:17:25] Codeex, lets it run for an hour, and it
[00:17:27] solves it. What What did you guys do? We
[00:17:30] have this strong sort of mission here at
[00:17:32] OpenAI to you know basically to build
[00:17:34] AGI. Um and so we we think a lot about
[00:17:38] what how can we shape the product so
[00:17:40] that it can scale right you know earlier
[00:17:43] I was mentioning like hey like if you're
[00:17:44] an engineer you should be getting help
[00:17:45] from from AI like thousands of times per
[00:17:48] day right and so we thought a lot about
[00:17:50] the primitives for that when we launched
[00:17:52] our first version of codeex uh which was
[00:17:54] Codex cloud and that was basically a
[00:17:57] product that had its own computer lives
[00:17:58] in the cloud you could delegate to it
[00:18:00] and you know the sort of the coolest
[00:18:02] part about that was you could run many
[00:18:03] many tasks in parallel
[00:18:05] But some of the challenges that we saw
[00:18:08] are that it's a little bit harder to set
[00:18:11] that up both in terms of like
[00:18:13] environment configuration like giving
[00:18:14] the model the tools it needs to validate
[00:18:16] changes and to learn how to prompt in
[00:18:18] that way. And sort of my my analogy for
[00:18:21] this is going back to this teammate
[00:18:22] analogy. It's like if you hired a
[00:18:23] teammate but you're never allowed to get
[00:18:26] on a call with them and you can only go
[00:18:27] back and forth, you know, asynchronously
[00:18:30] over time. like that works for some
[00:18:31] teammates and eventually that's actually
[00:18:33] how you want to spend most of your time.
[00:18:35] So that's still the future, but it's
[00:18:36] hard to initially adopt.
[00:18:39] So we still have that vision of like
[00:18:40] that's what we're trying to get you to a
[00:18:42] teammate that you delegate to and then
[00:18:43] is proactive and we're seeing that
[00:18:45] growing. But the key unlock is actually
[00:18:48] first you need to land with users in a
[00:18:50] way that's like much more intuitive and
[00:18:51] like trivial to get value from. So the
[00:18:55] way that most people discover like the
[00:18:56] vast majority of users discover codeex
[00:18:58] today is either they download an IDE
[00:19:00] extension or they run it in their CLI
[00:19:03] and the agent works there with you on
[00:19:05] your computer interactively and uh it
[00:19:08] works within a sandbox which is actually
[00:19:09] like a really cool piece of tech to to
[00:19:11] help that be safe and secure but it has
[00:19:13] access to all those dependencies. So if
[00:19:16] the agent needs to do something like it
[00:19:17] needs to run a command it can do so
[00:19:19] within the sandbox. we don't have to set
[00:19:20] up any environment and if it's a command
[00:19:22] that doesn't work in the sandbox it can
[00:19:23] just ask you and so you can get into
[00:19:25] this like really strong feedback loop
[00:19:27] using the model and then over time like
[00:19:29] our team's job is to like help turn that
[00:19:31] feedback loop into you sort of as a
[00:19:34] byproduct of using the product
[00:19:35] configuring it so that you can then be
[00:19:37] delegating to it down the line and again
[00:19:39] analog you keep coming back to it but
[00:19:41] like if you hire a teammate and you ask
[00:19:43] them to do work but they you just give
[00:19:44] them like a fresh computer from the
[00:19:46] store it's going to be hard for them to
[00:19:47] do their job right but if as you work
[00:19:49] with them side by side. You could be
[00:19:51] like, "Oh, you don't have a password for
[00:19:52] this service we use. Here's the password
[00:19:54] for this service." You know, yeah, don't
[00:19:56] worry. Feel free to run this command.
[00:19:57] Then it's like much easier for them to
[00:19:59] then go off and do work for hours
[00:20:00] without you. So, what I'm hearing is the
[00:20:03] initial version of Codeex was almost too
[00:20:04] far in the future. It's like a remote in
[00:20:06] the cloud uh agent that's coding for you
[00:20:09] asynchronously. And what you did is
[00:20:11] okay, let's actually come back a little
[00:20:13] bit. Let's integrate into the way
[00:20:15] engineers already integrate into IDs and
[00:20:17] locally and help them kind of on ramp to
[00:20:20] this new world. Totally. And this was it
[00:20:23] was quite interesting because we we dog
[00:20:26] food product a ton at OpenAI. So you
[00:20:28] know dog food as in we use our own
[00:20:30] product and so Codex has been
[00:20:32] accelerating OpenAI over the course of
[00:20:34] the entire year and the cloud product
[00:20:36] was a massive accelerant to the company
[00:20:38] as well. Um it just turns out that this
[00:20:42] is one of those places where the signal
[00:20:44] we got from dog fooding is a little bit
[00:20:46] different from the signal you get from
[00:20:47] like the general market because at
[00:20:48] OpenAI you know we train reasoning
[00:20:50] models all day and so we're very used to
[00:20:52] this kind of prompting thing and like
[00:20:54] you know think up front run things
[00:20:55] massively in parallel and uh you know it
[00:20:59] would take some time and then come back
[00:21:00] to it later asynchronously and so you
[00:21:03] know now when we build we still get a a
[00:21:04] ton of signal from dog footing
[00:21:06] internally but uh you know we're also
[00:21:09] very cognizant of like the different
[00:21:10] ways that different audiences use the
[00:21:12] product. That's really funny. It's like
[00:21:14] live in the future but maybe not too far
[00:21:16] in the future. And I could see how
[00:21:17] everyone open AI is living very far in
[00:21:19] the future and sometimes that won't that
[00:21:21] won't work for everyone.
[00:21:22] >> Yeah. What about just like uh
[00:21:25] intelligence training data? I don't
[00:21:26] know. Is there something else that
[00:21:28] helped Codeex accelerate its ability to
[00:21:31] actually code? Is it like better,
[00:21:32] cleaner data? Is it more just models
[00:21:35] advancing? Is there anything else that
[00:21:36] really helped accelerate? Yeah. So
[00:21:38] there's like a few components here. Um I
[00:21:41] guess you know you were mentioning
[00:21:42] models and the models have improved a
[00:21:44] ton. In fact um just last Wednesday we
[00:21:47] shipped GPD 5.11 CEX Max a very you know
[00:21:50] accurately named model. Uh that is that
[00:21:54] is awesome. It is awesome both because
[00:21:56] it is um for any given task that you
[00:21:59] were using GPD 5.1 codecs for it's like
[00:22:01] you know roughly uh 30% faster at
[00:22:04] accomplishing that task but also it
[00:22:06] unlocks a ton of intelligence. So if you
[00:22:08] use it at our higher reasoning levels,
[00:22:10] it's just like even smarter. Um, and you
[00:22:12] know that that feedback that or that
[00:22:13] tweet you were saying like Karpathi made
[00:22:15] about like, hey, give us your gnarliest
[00:22:16] bugs like you know obviously there's a
[00:22:18] ton going on in the market right now,
[00:22:20] but like Codex Max is definitely like
[00:22:22] carrying that mantle of uh, you know,
[00:22:24] tackling the hardest bugs. Um, so that
[00:22:26] is that is super cool. But I will say
[00:22:28] it's like some of what how we're
[00:22:31] thinking about this is evolving a little
[00:22:32] bit from being like yeah we're just
[00:22:33] going to think about the model and like
[00:22:35] let's just like train the best model to
[00:22:37] really thinking about like what is an
[00:22:38] agent actually overall right and you
[00:22:42] know I'm not going to try to define
[00:22:43] agent exactly but at least the stack
[00:22:45] that we think of it as having is it's
[00:22:46] like you have this model really smart
[00:22:48] reasoning model that knows how to do a
[00:22:51] specific kind of task really well. So we
[00:22:52] can talk about how we make that
[00:22:53] possible. But then actually we need to
[00:22:55] serve that model through an API into a
[00:22:59] harness. And both of those things also
[00:23:01] have a really big role here. So for
[00:23:03] instance, one of the things uh that
[00:23:05] we're really proud of is you can have
[00:23:06] GP5.1 CX max work for really long
[00:23:09] periods of time. That's not like normal,
[00:23:11] but you can set it up to do that or that
[00:23:13] might happen. But now routinely we'll
[00:23:14] hear about people saying like yeah, it
[00:23:16] ran like overnight or it ran for 24
[00:23:18] hours. M
[00:23:18] >> and so you know for a model to work
[00:23:20] continuously for that amount of time
[00:23:22] it's going to exceed its context window
[00:23:24] and so we have a solution for that which
[00:23:25] we call compaction. Um but compaction is
[00:23:29] actually a feature that uses like all
[00:23:30] three layers of that stack. So you need
[00:23:33] to have a model that has a concept of
[00:23:36] compaction and knows like okay as I
[00:23:37] start to approach this context window I
[00:23:39] might be asked to like prepare to be run
[00:23:41] in a new context window. And then at the
[00:23:43] API layer, you need an API that like
[00:23:45] understands this concept and like has an
[00:23:47] endpoint that you can hit to do this
[00:23:48] change. And at the harness layer, you
[00:23:50] need a harness that can like prepare the
[00:23:51] payload for this to be done. And so like
[00:23:53] shipping this compaction feature that
[00:23:55] now just like made this behavior
[00:23:56] possible to like anyone using codecs
[00:23:58] actually been working across all three
[00:23:59] things. And I think that's like
[00:24:00] increasingly going to be true. Another
[00:24:03] maybe like underappreciated version of
[00:24:06] this is is if you think about all the
[00:24:08] different coding products out there,
[00:24:09] they all have like very different tool
[00:24:10] harnesses with like very different
[00:24:12] opinions on how the model should work.
[00:24:14] And so if you want to train a model to
[00:24:16] be good at like all the different ways
[00:24:17] uh it could work. Like you know maybe
[00:24:19] you have a strong opinion that it should
[00:24:20] work using semantic search, right? Maybe
[00:24:23] you have a strong opinion that it should
[00:24:24] like call bespoke tools or maybe you
[00:24:26] have like in our case a strong opinion
[00:24:27] that it should just use like the shell
[00:24:29] work in the terminal. You know, you can
[00:24:32] be much you can move much faster if
[00:24:33] you're just optimizing for one of those
[00:24:34] worlds, right? And so the way that we
[00:24:37] built codeex is that it just uses the
[00:24:38] shell. But in order to make that like
[00:24:40] safer and secure, we uh have a sandbox
[00:24:43] that the model is used to operating in.
[00:24:45] So I think one of the biggest
[00:24:46] accelerants to go all the way back to
[00:24:47] your to your answer question Russian is
[00:24:49] just like we're building all three
[00:24:50] things in parallel and like kind of
[00:24:52] tuning each one and um you know
[00:24:54] constantly experimenting with how those
[00:24:56] things work with like a tightly
[00:24:57] integrated product and research team.
[00:24:59] How do you think you win in this space?
[00:25:02] Do you think it it'll event it'll always
[00:25:04] be this kind of like race with other
[00:25:06] models constantly kind of leaprogging
[00:25:08] each other? Do you think there's a world
[00:25:09] where someone just t runs away with it
[00:25:11] and no one else can ever catch up? Is
[00:25:13] there like a path to just we win?
[00:25:15] >> Again comes back to this idea of like
[00:25:16] building a teammate and not just a
[00:25:19] teammate that you know uh participates
[00:25:22] in team planning and prioritization. Not
[00:25:24] just a teammate that you know really
[00:25:26] tests its code and like helps you
[00:25:27] maintain and deploy. But even a teammate
[00:25:29] you know like if you think again an
[00:25:31] engineering teammate they can also like
[00:25:32] schedule a calendar invite right or move
[00:25:34] standup or do whatever right. And so in
[00:25:38] my mind, if we just imagine that every
[00:25:42] day or every week some like crazy new
[00:25:44] capability is just going to be deployed
[00:25:46] by a research lab, it's just impossible
[00:25:48] for us like you know as humans to keep
[00:25:50] up and like use all this technology. And
[00:25:52] so I think we need to get to this world
[00:25:54] where you kind of just have like an AI
[00:25:57] teammate or super assistant that you
[00:25:59] just talk to and it just knows how to be
[00:26:02] helpful like on its own, right? And so
[00:26:04] you don't you don't have to be like
[00:26:06] reading the latest tips for how to use
[00:26:07] it. You just like you've plugged it in
[00:26:08] and it just provides help. And so that's
[00:26:11] kind of the shape of what I think we're
[00:26:13] building. And I think that will be like
[00:26:14] a very sticky like winning product if we
[00:26:16] can do so. So the shape that in my head
[00:26:18] at least I have is that we build you
[00:26:21] know maybe a fun topic is like is chat
[00:26:23] the right interface for AI? I actually
[00:26:24] think chat is a very good interface when
[00:26:27] you don't know what you're supposed to
[00:26:28] use it for. uh in the same way that if I
[00:26:30] think of like I'm like on a teams or in
[00:26:32] Slack with a teammate, chat is pretty
[00:26:34] good. I can ask for whatever I want,
[00:26:35] right? It's like it's kind of the the
[00:26:37] common denominator for everything. So
[00:26:39] you can chat with a super assistant
[00:26:40] about whatever topic you want, whether
[00:26:42] it be coding or not. And then if you are
[00:26:45] like a functional expert in a specific
[00:26:47] domain such as coding, there's like a
[00:26:49] guey that you can pull up to go really
[00:26:52] deep and like look at the code and like
[00:26:54] work with the code. So I think like what
[00:26:55] we need to build as open AI is basically
[00:26:59] this idea of like you have chat chatpt
[00:27:00] PT and that is a tool that's like
[00:27:02] ubiquitously available to like everyone.
[00:27:04] You start using it even like outside of
[00:27:06] work right to just help you. You become
[00:27:08] very comfortable with the idea of being
[00:27:09] accelerated with AI. And so then you get
[00:27:12] to work and you just can naturally just
[00:27:13] yeah I'm just going to ask it for this
[00:27:15] and I don't need to know about all the
[00:27:16] connectors or like all the different
[00:27:18] features. I'm just going to ask it for
[00:27:19] help and it'll surface to me the the
[00:27:21] best way that it can help at this point
[00:27:23] in time and maybe even chime in when I
[00:27:24] didn't ask it for help. Um, so in my
[00:27:27] mind, if we can get to that, I think
[00:27:28] that's, you know, that's how we we
[00:27:30] really build like the winning product.
[00:27:32] This is so interesting because with the
[00:27:34] my chat with Nick Charlie, the head of
[00:27:35] chat JPT, I think he shared that the
[00:27:37] original name for Chat JPT was super
[00:27:39] assistant or something like that.
[00:27:41] >> Yeah.
[00:27:42] >> And it's interesting that there's like
[00:27:44] that approach to the super assistant and
[00:27:46] then there's this codeex approach. It's
[00:27:48] almost like the B TOC version and the
[00:27:49] B2B version. And what I'm hearing is the
[00:27:52] idea here is okay, you start with coding
[00:27:53] and building and then it's doing all
[00:27:55] this other stuff for you, scheduling
[00:27:56] meetings, I don't know, probably posting
[00:27:58] in Slack, uh I don't know, shipping
[00:28:01] designs, I don't know. Is that is the
[00:28:02] idea there? This is like the the
[00:28:04] business version of ChatGpt in a sense.
[00:28:06] Or is there or is there something else
[00:28:08] there?
[00:28:08] >> Yeah. So, you know, so we're getting to
[00:28:10] the like the like one-year time horizon
[00:28:12] conversation. A lot of this might happen
[00:28:14] sooner, but in terms of fuzziness, I
[00:28:16] think we're at the one year. So I'll
[00:28:17] give you like a contention in like the
[00:28:19] plausible way we get there, but as for
[00:28:21] how it happens, who knows? So basically,
[00:28:23] if we're going to build a super
[00:28:24] assistant, it has to be able to do
[00:28:26] things, right? So like we're going to
[00:28:28] have a model and it's going to be able
[00:28:29] to do stuff affecting your world.
[00:28:31] >> And one of the learnings I think we've
[00:28:33] seen over the past year or so is that
[00:28:36] for models to do stuff, they're much
[00:28:38] more effective when they can use a
[00:28:39] computer,
[00:28:41] right? Okay. So now we're like, okay, we
[00:28:43] need the super assistant that can use a
[00:28:45] computer, right? or many computers. And
[00:28:47] now the question is, okay, well, how
[00:28:48] should it use the computer, right? And
[00:28:50] there's lots of ways to use a computer.
[00:28:52] Uh, you know, you could try to hack the
[00:28:54] OS and like use accessibility APIs.
[00:28:56] Maybe a bit easier is you could point
[00:28:57] and click. That's a little slow, you
[00:28:59] know, and, uh, unpredictable sometimes.
[00:29:02] Um, and another way, it turns out the
[00:29:04] best way for models to use computers is
[00:29:06] simply to write code, right? And so
[00:29:08] we're kind of getting to this idea where
[00:29:09] like, well, if you want to build any
[00:29:10] agent, maybe you should be building a
[00:29:12] coding agent. And maybe to the user, a
[00:29:15] nontechnical user, they won't even know
[00:29:17] they're using a coding agent. The same
[00:29:18] way that no one thinks about are they
[00:29:19] using the internet or not, which is
[00:29:20] they're more just like is Wi-Fi on?
[00:29:22] Right? So I think that what we're doing
[00:29:25] with codeex is we're building a software
[00:29:27] engineering teammate. And as part of
[00:29:29] that, we're kind of building an agent
[00:29:30] that can use uh a computer by writing
[00:29:33] code. And so we're already seeing like
[00:29:36] some pull for this. It's like quite
[00:29:37] early, but we're starting to see people
[00:29:39] like who are using codeex for like
[00:29:40] coding adjacent product purposes.
[00:29:43] And so as that develops, I think we'll
[00:29:46] just naturally see that like, oh, it
[00:29:47] turns out like we should just always
[00:29:48] have the agent write code if there is a
[00:29:50] coding way to solve a problem instead
[00:29:51] of, you know, even if you're doing a
[00:29:53] financial analysis, right? Like maybe
[00:29:54] write some code for that. So basically
[00:29:56] like, you know, you were like, hey, is
[00:29:57] this like the two ends of of uh of this
[00:29:59] product for the super assistant, right,
[00:30:00] of CHCH PT? In my mind, like just coding
[00:30:03] is a core competency of any agent,
[00:30:05] including Chach PT. And so like what
[00:30:06] really what we think we're building is
[00:30:08] like that competency. But so here's
[00:30:10] here's like the really cool thing about
[00:30:11] agents writing code is that you can
[00:30:13] import code right code is like
[00:30:16] composable interoperable right because
[00:30:19] if if we you know one very reductive
[00:30:21] view we could have for an agent is it's
[00:30:23] just going to be given a computer and
[00:30:25] it's just going to like point and click
[00:30:26] and you know go around but you know that
[00:30:29] is the future and then how we get there
[00:30:32] is difficult to sort of chart a path
[00:30:34] because a lot of the questions around
[00:30:36] building agents aren't like can the
[00:30:37] agent do it but it's more about well how
[00:30:41] can we help the agent understand the
[00:30:42] context that it's working in and like
[00:30:44] the team that's using it you know
[00:30:46] probably has a way that they like to do
[00:30:47] things they have guidelines they
[00:30:49] probably want certain deterministic
[00:30:50] guarantees about what the agent can or
[00:30:52] cannot do or they want to know that the
[00:30:54] agent understands sort of this detail
[00:30:57] like an example would be you know if
[00:30:59] we're looking at a crash reporting tool
[00:31:02] hitting a connector for it every sub
[00:31:04] team is probably has a different meta
[00:31:06] prompt for like how they want the
[00:31:07] crashes to be analyzed ized, right? And
[00:31:10] so we start to get to this thing where
[00:31:12] like, yeah, we have this agent sitting
[00:31:13] in front of a computer, but we need to
[00:31:15] make that configurable for the team or
[00:31:17] for the user, right? And let them like
[00:31:19] stuff that the agent does often, we
[00:31:21] probably just want to like build in as a
[00:31:22] competency that this agent has that it
[00:31:24] can do. So I think we end up with this
[00:31:27] generalizable thing that you were saying
[00:31:29] of like an agent that can just write its
[00:31:31] own scripts for whatever it wants to do.
[00:31:33] But I think that the the really key part
[00:31:36] here is can we make it so that
[00:31:39] everything that the agent has to do
[00:31:40] often or that it does well we can just
[00:31:42] like remember and store so that the
[00:31:44] agent doesn't have to write a script for
[00:31:46] that again. Right. Or maybe like if I
[00:31:47] just joined a team and you are already
[00:31:49] on the same team as me. I can just like
[00:31:51] use all those scripts that the agents
[00:31:52] had written already.
[00:31:53] >> Yeah. It's like if this is our teammate
[00:31:56] uh we can they can share things that
[00:31:57] it's learned from working with other
[00:31:59] people at the company. Just makes sense
[00:32:00] as a metaphor.
[00:32:01] >> Yeah. It feels like you're in the uh
[00:32:04] Karpathy camp of agents today are not
[00:32:05] that great and mostly slop and maybe in
[00:32:08] the future they'll be awesome. Does that
[00:32:09] resonate?
[00:32:10] >> I think so. I think coding agents are
[00:32:12] pretty great. I think
[00:32:14] >> uh ton of value,
[00:32:15] >> right? Yep.
[00:32:16] >> And then I think like agents outside of
[00:32:19] coding, it's still like very early and
[00:32:21] you know, this is just my opinion, but I
[00:32:23] think they're going to get a whole lot
[00:32:24] better once they can use coding too and
[00:32:26] like in a composable way.
[00:32:28] This is it's kind of the fun part of
[00:32:29] like when you're building for software
[00:32:30] engineers. Like I at my startup we were
[00:32:33] building for software engineers too for
[00:32:34] a lot of that journey and they're just
[00:32:36] such a fun audience to build for because
[00:32:39] you know they also like building for
[00:32:41] themselves and are often like even more
[00:32:43] creative than we are and thinking about
[00:32:44] how to use the technology. Um and so
[00:32:47] like by building for software engineers
[00:32:48] you get to just observe a ton of
[00:32:50] emergent behaviors and like things that
[00:32:52] you should do and build into the
[00:32:53] product. I love how you you say that
[00:32:55] because a lot of people building for
[00:32:56] engineers get really annoyed because the
[00:32:57] engineers are so they're just always
[00:32:59] complaining about stuff. They're like,
[00:33:00] "Ah, that sucks. Why'd you build it this
[00:33:02] way?" I love that you enjoy it, but I
[00:33:04] think it's probably because you're
[00:33:05] building such an amazing tool for
[00:33:06] engineers that can actually solve
[00:33:08] problems and just, you know, code for
[00:33:11] them. Um, kind of along those lines, you
[00:33:13] know, there's always this talk of what
[00:33:15] will happen with jobs, engineers,
[00:33:16] coding, do you have to learn coding, all
[00:33:18] these things? Uh clearly the way you're
[00:33:20] describing it is it's a teammate. It's
[00:33:21] going to work with you, make you more
[00:33:22] superhuman. It's not going to replace
[00:33:24] you with the way you just think about
[00:33:26] the impact on the field of engineering
[00:33:28] having this super intelligent
[00:33:31] engineering teammate. I think there's
[00:33:33] there's two sides to it, but the one we
[00:33:35] were just talking about is this idea
[00:33:36] that maybe every agent should actually
[00:33:39] use code and be a coding agent. And in
[00:33:43] my mind, that's just like a small part
[00:33:44] of this like broader idea that like,
[00:33:46] hey, as we make code even more
[00:33:47] ubiquitous, I mean, you could probably
[00:33:48] claim it's ubiquitous today, even pre
[00:33:50] AAI, right? But as we make code even
[00:33:51] more ubiquitous, it's actually just
[00:33:53] going to be used for many more purposes.
[00:33:56] And so there's just going to be a ton
[00:33:58] more need for people with this like
[00:33:59] humans with this competency. So that's
[00:34:02] my view. I think this is like quite a
[00:34:05] complex topic. So, you know, it's
[00:34:07] something we talk about a lot and we
[00:34:08] have to kind of see how it pans out. But
[00:34:10] I think what we can do what we can do
[00:34:12] basically as a product team building in
[00:34:13] the space is just try to always think
[00:34:15] about how are we building a tool so that
[00:34:17] it feels like we're like maximally
[00:34:18] accelerating uh people you know rather
[00:34:21] than building a tool that makes it like
[00:34:24] more unclear what you should do as the
[00:34:25] human right like I think like to to you
[00:34:29] know give an example right now like
[00:34:31] nowadays when you work with a coding
[00:34:33] agent um it writes a ton of code but it
[00:34:35] turns out writing code is actually one
[00:34:36] of the most fun parts of software
[00:34:38] engineering for many software engineers.
[00:34:40] is so then you end up reviewing AI code,
[00:34:42] right? And that's often a less fun part
[00:34:45] of the job for many software engineers,
[00:34:47] right? And so I actually think like we
[00:34:49] see that like this this comes out plays
[00:34:51] out all the time in like a ton of micro
[00:34:53] decisions. And so we as a product team
[00:34:54] are always thinking about like okay, how
[00:34:55] do we make this more fun? How do we make
[00:34:56] you feel more empowered whereas it's not
[00:34:58] working and I I would argue that like
[00:35:00] reviewing agent written code is like a
[00:35:01] place that today is like less fun. And
[00:35:04] so you know then I think okay what can
[00:35:06] we do about that? Well, we can ship a
[00:35:07] code review feature that like helps you
[00:35:09] build confidence in the Irw written
[00:35:10] code. Okay, cool. You know, another
[00:35:12] thing we can do is we can make it so
[00:35:13] that the agent's like better able to
[00:35:14] validate its work. And you know, it gets
[00:35:17] all the way down into like micro
[00:35:18] decisions like if you're going to have
[00:35:20] the an agent capability to validate work
[00:35:23] and let's say you have like I'm thinking
[00:35:24] of Codex web right now like you have a a
[00:35:26] pane that sort of reflects the work the
[00:35:28] agent did. What do you see first? Do you
[00:35:30] see the diff or do you see the image
[00:35:31] preview of the code it wrote? Right? And
[00:35:34] you know, I think if you're thinking
[00:35:35] about this from perspective like how do
[00:35:36] I empower the human? How do I make them
[00:35:38] feel like as as accelerated as possible
[00:35:40] like you obviously see the image first,
[00:35:42] right? You shouldn't be reviewing the
[00:35:43] code unless first you know you've seen
[00:35:45] the image unless maybe it's being like
[00:35:46] reviewed by an AI and now it's time for
[00:35:48] you to take a look. When I had uh
[00:35:49] Michael Charel, the CEO of Cursor on the
[00:35:51] podcast, he he had this kind of vision
[00:35:53] of us moving to something beyond code.
[00:35:57] And I've seen this rise of something
[00:35:58] called specd driven development where
[00:36:00] you kind of just write the spec and then
[00:36:02] the code, you know, the AI writes code
[00:36:04] for you. And so you kind of start
[00:36:05] working at this higher abstraction
[00:36:06] level. Is that something you see where
[00:36:09] we're going? Just like engineers not
[00:36:10] having to actually write code or look at
[00:36:12] code and there's going to be this higher
[00:36:13] level of abstraction that we focus on.
[00:36:16] Yeah, I mean I think I think there's
[00:36:18] like constantly these levels of
[00:36:19] abstraction and they're actually already
[00:36:20] played out today, right? Like today like
[00:36:23] coding agents mostly it's like prompt to
[00:36:26] patch right we're starting to see people
[00:36:29] doing like spec driven development or
[00:36:31] like planned driven development that's
[00:36:32] actually one of the ways when people ask
[00:36:34] like hey how do you run codex on a
[00:36:35] really long task well it's like often
[00:36:37] collaborate with it first to write like
[00:36:38] a plan MD like a markdown file that's
[00:36:40] your plan and once you're happy with
[00:36:42] that then you ask it to go off and do
[00:36:44] work and if that plan has verifiable
[00:36:46] steps it'll like work for much longer.
[00:36:48] Um so we're totally seeing that. I think
[00:36:51] spec driven development is like an
[00:36:52] interesting idea. It's not clear to me
[00:36:54] that it'll work out that way because a
[00:36:56] lot of people don't write like don't
[00:36:57] like writing specs either, but it seems
[00:37:00] plausible that some some people will
[00:37:02] work that way. You know, like a a bit of
[00:37:05] a joke idea though is like if you think
[00:37:06] of like um the way that many teams work
[00:37:09] today, they're they often like don't
[00:37:10] necessarily have specs, but the team is
[00:37:13] just really self-driven and so stuff
[00:37:14] just gets done. And so almost that is
[00:37:15] like I'm coming up with this on the spot
[00:37:17] so it's you know not a good name but
[00:37:18] like chatterdriven development where
[00:37:21] it's just like stuff is happening you
[00:37:22] know on social media and like in your
[00:37:24] team communications tools and then as a
[00:37:26] result like code gets written and
[00:37:28] deployed right so yeah I think I'm a
[00:37:31] little bit more oriented in that way of
[00:37:33] you know I don't even necessarily want
[00:37:35] to have to write a spec like sometimes I
[00:37:37] want to only if I like writing specs
[00:37:40] right uh other times I might just want
[00:37:42] to say like hey here's like the
[00:37:44] customer, you know, service channel and
[00:37:45] like tell me what's interesting to know,
[00:37:47] but if it's a small bug, just fix it. I
[00:37:49] don't want to have to write a spec for
[00:37:50] that, right?
[00:37:51] >> I have this sort of
[00:37:53] uh hypothetical future uh that I like to
[00:37:57] share sometimes with people as a
[00:37:58] provocation, which is like in a world
[00:38:00] where we have like truly amazing agents,
[00:38:01] like what does it look like to be a
[00:38:02] soloreneur?
[00:38:04] Um, and uh, you know, one terrible idea
[00:38:07] for how it could look is that it's
[00:38:08] actually there's a mobile app and um,
[00:38:12] every idea that the agent has to do is
[00:38:14] just like vertical video on your phone
[00:38:17] and then you can like swipe left if you
[00:38:19] think it's a bad idea and you can like
[00:38:21] swipe right if it's a good idea and like
[00:38:22] you can press and hold and like speak to
[00:38:24] your phone if you want to get feedback
[00:38:26] on the idea before you swipe, you know.
[00:38:28] So in this world like basically what
[00:38:30] your job is just to like plug in this
[00:38:31] app into like every single like signal
[00:38:33] system you know system of record and
[00:38:36] then you just sort of sit back and like
[00:38:37] swipe. I don't know.
[00:38:39] >> I love this. So this is like Tinder
[00:38:40] meets Tik Tok meets codeex.
[00:38:42] >> It's pretty terrible.
[00:38:43] >> No, this is great. So the idea here is
[00:38:45] this thing is this agent is watching and
[00:38:47] right listening to you paying attention
[00:38:49] to the market your users and it's like
[00:38:51] cool here's something I should do. It's
[00:38:53] like a proactive engineer just like here
[00:38:54] we should build this feature fix this
[00:38:56] thing.
[00:38:56] >> Exactly. I think they're communicating
[00:38:59] with you in like the lowest like the
[00:39:01] gyms like the modern way to communicate.
[00:39:05] >> Yeah.
[00:39:05] >> Swipe left or right and in vertical feed
[00:39:08] and then the Sora video. Okay. So I see
[00:39:10] how this all connects now. I see.
[00:39:12] >> Yeah. To be clear, we're not building
[00:39:13] that but like you know it's a fun idea.
[00:39:15] I mean you see you know like in this
[00:39:17] example though like one of the things
[00:39:18] that it's doing is it's consuming
[00:39:19] external signals right. I think the
[00:39:21] other really interesting thing is like
[00:39:23] if we think about like what is the most
[00:39:24] successful like AI product to date
[00:39:28] um I would argue um it's funny actually
[00:39:32] not to confuse things at all but like
[00:39:34] the first time we used the the brand
[00:39:36] codeex at OpenAI was actually the model
[00:39:38] powering GitHub copilot. This is like
[00:39:39] way back in the day, years ago. And so
[00:39:42] we decided to reuse that that brand
[00:39:43] recently um because it's just so good,
[00:39:45] you know, codeex code execution. But I
[00:39:48] think actually like autocomp completion
[00:39:50] and IDEs is like one of the most
[00:39:51] successful AI products to date. And part
[00:39:54] of what's so magical about it is that
[00:39:58] when the it can surface like ideas for
[00:40:01] helping you really rapidly. When it's
[00:40:03] right, you're accelerated. When it's
[00:40:05] wrong, it's not like that annoying. It
[00:40:07] can be annoying, but it's not that
[00:40:08] annoying, right? And so you can create
[00:40:10] this like mixed initiative system that's
[00:40:12] like contextually responding to like
[00:40:14] what you're attempting to do. And so in
[00:40:17] my mind, this is like a really
[00:40:19] interesting thing for us as open as
[00:40:21] we're building. So for instance, you
[00:40:23] know, when I think about launching a
[00:40:25] browser, which we did with Atlas, right?
[00:40:27] Like in my mind, one of the really
[00:40:29] interesting things we can then do is we
[00:40:31] can then like contextually surface like
[00:40:33] ways that we can help you as you're
[00:40:35] going about your day, right? And so we
[00:40:37] break out of this like, you know, we're
[00:40:39] just looking at code or we're just in
[00:40:40] your terminal um into this idea that
[00:40:43] like, hey, like a real teammate is
[00:40:44] dealing with a lot more than just code,
[00:40:46] right? They're dealing with a lot of
[00:40:47] things that are web content. So like,
[00:40:49] you know, how can we help you with that?
[00:40:51] >> Man, there's so much there and I love
[00:40:53] this. Okay, so autocomplete on web with
[00:40:55] the browser. That's so interesting. just
[00:40:56] like here's all the things that we can
[00:40:58] help you with as you're browsing and
[00:41:00] going about your day. I want to talk
[00:41:01] about Atlas. I'll come back to that. Uh
[00:41:03] codeex code execution. Did not know
[00:41:05] that. That's really clever. I I get it
[00:41:08] now. Okay. And then this chatter, what
[00:41:10] is a chatter driven development? Uh I
[00:41:12] had a No, this is a really good idea,
[00:41:14] but it reminds me I had John Gon on the
[00:41:16] podcast, CTO of Block, and they they
[00:41:19] have this product called Goose, which is
[00:41:20] their own internal agent thing. And he
[00:41:24] talked about an engineer at block just
[00:41:27] uh has goose watch him with like his
[00:41:30] screen and listens to every meeting and
[00:41:33] proactively does work that he should
[00:41:36] will probably want to do. So ships a PR
[00:41:38] sends an email drafts a Slack message.
[00:41:41] So he's doing exactly what you're
[00:41:42] describing in in kind of a very early
[00:41:44] way.
[00:41:45] >> Yeah, that's super interesting. And you
[00:41:47] know, I bet you the So, if we go if we
[00:41:49] went and asked them what the bottleneck
[00:41:50] to that productivity is, did did they
[00:41:52] share what it is?
[00:41:54] >> Uh, probably looking at it just making
[00:41:55] sure this is the right the right thing
[00:41:57] to do. Yeah.
[00:41:58] >> Yeah. So, like we see this now like we
[00:41:59] have a Slack integration for Codex.
[00:42:01] People love, you know, if there's like
[00:42:02] some thing that you need to do quickly.
[00:42:04] People just like at mentioned Codex like
[00:42:06] why do you think this bug is happening?
[00:42:07] Right. Doesn't have to be an engineer.
[00:42:08] Even like maybe you know data scientists
[00:42:10] often here are using Codex a ton to just
[00:42:12] like answer questions like why do you
[00:42:14] think this metric moved? What happened?
[00:42:16] So questions you you get the answer
[00:42:18] right back in Slack. It's amazing, super
[00:42:19] useful. But when it's as for when it's
[00:42:22] writing code, then you have to go back
[00:42:24] and look at the code, right? And so the
[00:42:27] real like I think bottleneck right now
[00:42:29] is like validating that the code worked
[00:42:30] and like writing code review.
[00:42:33] So in my mind, if we wanted to get to
[00:42:34] something like uh you know that uh a
[00:42:36] friend you were talking about world, I
[00:42:38] think we we really need to figure out
[00:42:40] how to get people to configure their
[00:42:42] coding agents to be much more autonomous
[00:42:44] on those later stages of the work. It
[00:42:46] makes sense like you said writing code.
[00:42:48] I used to be an engineer as an engineer
[00:42:49] for 10 years. Really fun to write code.
[00:42:51] Really fun to just get in the flow,
[00:42:52] build, architect, test. Not so fun to
[00:42:55] look at everyone else's code and just
[00:42:56] have to go through and be on the hook if
[00:42:58] it is doing something dumb that's going
[00:43:00] to take down production. And now that
[00:43:02] building has become easier, what I've
[00:43:03] always heard from companies that are
[00:43:04] really at the cutting edge of this is
[00:43:06] the bottleneck is now like figuring out
[00:43:08] what to build and then it's at the end
[00:43:09] of like, okay, we have all this all 100
[00:43:11] hours to review. Who's going to go
[00:43:13] through all that?
[00:43:14] >> Right. Yeah.
[00:43:17] This episode is brought to you by Jira
[00:43:18] product discovery. The hardest part of
[00:43:20] building products isn't actually
[00:43:22] building products. It's everything else.
[00:43:24] It's proving that the work matters,
[00:43:26] managing stakeholders, trying to plan
[00:43:28] ahead. Most teams spend more time
[00:43:30] reacting than learning, chasing updates,
[00:43:32] justifying road maps, and constantly
[00:43:34] unblocking work to keep things moving.
[00:43:36] Jira product discovery puts you back in
[00:43:39] control. With Jira product discovery,
[00:43:41] you can capture insights and prioritize
[00:43:43] high impact ideas. It's flexible, so it
[00:43:46] adapts to the way your team works and
[00:43:47] helps you build a road map that drives
[00:43:49] alignment, not questions. And because
[00:43:51] it's built on Jira, you can track ideas
[00:43:53] from strategy to delivery, all in one
[00:43:56] place. Less chasing, more time to think,
[00:43:58] learn, and build the right thing. Get
[00:44:01] Jirroduct Discovery for free at
[00:44:03] atlassian.com/lenny.
[00:44:06] That's atassian.com/lenny.
[00:44:08] What has the impact of Codex been on the
[00:44:11] way you operate as a product person, as
[00:44:13] a PM? It's clear how engineering is
[00:44:15] impacted. Uh, code is written for you.
[00:44:19] What has it done to the way you operate,
[00:44:21] the way PMs operate at at OpenAI? Yeah,
[00:44:24] I mean I think mostly I just feel like
[00:44:26] much more empowered.
[00:44:28] Um I've always been sort of more
[00:44:30] technical leaning PM and especially when
[00:44:32] I'm working on products for engineers, I
[00:44:34] feel like it's necessary to like you
[00:44:35] know dog food the product but even
[00:44:37] beyond that I I I just feel like I can
[00:44:39] do much much more as a PM. And uh you
[00:44:42] know Scott Beltski talks about this idea
[00:44:43] of like compressing the talent stack.
[00:44:45] I'm not sure if I've phrased that right,
[00:44:46] but it's basically this idea that like
[00:44:48] maybe the boundaries between these roles
[00:44:50] are a little bit like less needed than
[00:44:52] before because people can just do much
[00:44:54] more and every time you someone can do
[00:44:56] more you can like skip one communication
[00:44:58] boundary and make the team like that
[00:45:00] much more efficient, right? So I think I
[00:45:04] think we see it you know in a bunch of
[00:45:07] functions now but I guess since you
[00:45:09] asked about like product specifically uh
[00:45:11] you know now like answering questions
[00:45:13] much much easier you can know just ask
[00:45:15] codeex for thoughts on that uh a lot of
[00:45:18] like PM type work understanding what's
[00:45:20] changing again just ask codeex for help
[00:45:21] with that um prototyping is often faster
[00:45:25] than writing specs this is something
[00:45:27] that a lot of people have talked about I
[00:45:29] think something that I don't think it's
[00:45:31] super surprising But something that's
[00:45:32] slightly surprising is like we see like
[00:45:35] we're mostly building codecs for to
[00:45:36] write code that's going to be deployed
[00:45:37] to production but actually we see a lot
[00:45:40] of throwaway code written with codeex
[00:45:41] now. It's kind of going back to this
[00:45:43] idea of like you know ubiquitous code.
[00:45:45] So you'll see uh you know someone wants
[00:45:48] to do an analysis like if I want to
[00:45:49] understand something it's like okay just
[00:45:51] give codeex a bunch of data but then ask
[00:45:52] it to build like an interactive like
[00:45:54] data viewer for this data right you
[00:45:55] would that's just like too annoying to
[00:45:56] do in the past but now it's just like
[00:45:58] totally worth the time of just getting
[00:46:00] an agent to go do something. Um,
[00:46:02] similarly, I've seen like some pretty
[00:46:04] cool prototypes on our design team about
[00:46:06] like if you want to well like a designer
[00:46:09] basically wanted to build an animation
[00:46:11] and this is the coin animation in codeex
[00:46:13] and it was like normally it'd be too
[00:46:15] annoying to program this animation. So
[00:46:17] they just vibe coded a animation editor
[00:46:20] and then they use the animation editor
[00:46:21] to build the animation which they then
[00:46:23] checked into the repo. Actually, our
[00:46:25] designers are there's a ton of
[00:46:26] acceleration there. And like speaking of
[00:46:28] compressing the town stack, I think our
[00:46:29] designers are very PM.
[00:46:31] So, you know, they they do ton of
[00:46:33] product work. And like they actually
[00:46:35] have like an entire like vibecoded sort
[00:46:38] of side prototype of the Codex app. And
[00:46:40] so, a lot of how we talk about things is
[00:46:41] like we'll have like a really quick jam
[00:46:43] because there's like 10,000 things going
[00:46:44] on. And then designer will like go think
[00:46:46] about how this should work, but instead
[00:46:48] of like talking about it again, they'll
[00:46:49] just like vibe code a prototype of that
[00:46:50] in their like standalone prototype.
[00:46:52] We'll play with it. If we like it,
[00:46:54] they'll vibe code that prototype into or
[00:46:56] vibe engineer that prototype into an
[00:46:59] actual PR to land. And then depending on
[00:47:01] their comfort with the codebase, like
[00:47:02] codeex CLI and Rust is a little harder.
[00:47:04] Maybe they'll like land it themselves or
[00:47:06] they'll like get close and then an
[00:47:07] engineer can help them like land the PR.
[00:47:09] Um, you know, we recently shipped the
[00:47:12] Sora Android app. Um and uh that was one
[00:47:15] of the most sort of mind-blowing
[00:47:18] examples of acceleration actually
[00:47:19] because usage of of codeex internally at
[00:47:22] open is obviously really really high but
[00:47:24] it's been growing uh over the course of
[00:47:27] the year both in terms of like now it's
[00:47:28] basically like all technical staff use
[00:47:30] it uh but even like the intensity and
[00:47:32] knowhow of how to make the most of
[00:47:33] coding agents has gone up by a ton and
[00:47:35] so the Sora Android app right like a
[00:47:37] fully new app we built it in 18 days it
[00:47:42] went from like zero to launch to
[00:47:44] employees and then 10 days later so 28
[00:47:46] days total we went to just like GA to
[00:47:49] the public and that was done just like
[00:47:51] with the help of Codex
[00:47:53] so pretty insane velocity I would say it
[00:47:56] was like a little bit I don't want to
[00:47:58] say easy mode but there is one thing
[00:48:01] that Codex is really good at if you're a
[00:48:03] company that's like building software on
[00:48:04] multiple platforms so you've already
[00:48:06] figured out like some of the underlying
[00:48:07] like APIs or systems asking codeex to
[00:48:10] like to port things over is really
[00:48:12] effective because it has like something
[00:48:14] you can go look at. And so the engineers
[00:48:15] on that team uh were basically having
[00:48:17] codeex go look at the iOS app, produce
[00:48:20] plans of work that needed to be done and
[00:48:22] then go implement those. And it was kind
[00:48:23] of looking at iOS and Android at the
[00:48:25] same time. And so you know basically it
[00:48:27] was like two weeks to launch to
[00:48:28] employees four weeks total. Insanely
[00:48:30] fast.
[00:48:31] >> What makes that even more insane is it
[00:48:33] was the it became the number one app in
[00:48:34] the app store.
[00:48:36] >> I don't this just boggles the mind.
[00:48:38] Okay. So
[00:48:39] >> yeah. So imagine releasing number one
[00:48:41] app on the app store with like a handful
[00:48:43] of engineers
[00:48:45] >> uh I think it was like
[00:48:47] >> two or three possibly
[00:48:49] >> uh in a handful of weeks. Yeah, this is
[00:48:53] absurd.
[00:48:55] So
[00:48:56] >> yeah, so that's a really fun um example
[00:48:59] of uh acceleration. And then like Atlas
[00:49:01] was the other one that I think um Ben
[00:49:04] did a podcast the the the engine on
[00:49:06] Atlas uh sharing a little bit of how we
[00:49:09] built there. You know many Atlas is is
[00:49:12] actually I mean it's it's a browser
[00:49:13] right and building a browser is really
[00:49:15] hard. Um and so we uh had to build a lot
[00:49:21] of difficult systems in order to do that
[00:49:23] and basically we got to the point where
[00:49:25] that team has a ton of power users of
[00:49:27] codecs right now. And um you know it got
[00:49:30] to the point where they they basically
[00:49:32] were you know we were talking to them
[00:49:33] about it because a lot of those
[00:49:34] engineers are people I used to work with
[00:49:36] before at my startup and so they'd say
[00:49:38] you know before this would have taken us
[00:49:39] like two to three weeks for two to three
[00:49:42] engineers and now it's like one engineer
[00:49:45] one week. Um so massive acceleration
[00:49:48] there as well. And what's quite cool is
[00:49:50] that uh you know we we shipped Atlas on
[00:49:52] on Mac first but now we're working on
[00:49:54] the Windows version. you know that so
[00:49:56] the team now is like ramping up on
[00:49:57] Windows and they're helping us make
[00:49:58] codecs better on Windows 2 which is
[00:50:01] admittedly earlier like just the model
[00:50:02] we we shipped last week is the first
[00:50:04] model that natively understands
[00:50:06] PowerShell. So you know PowerShell being
[00:50:09] uh the native like shell language on
[00:50:11] Windows. So yeah, it's been it's been
[00:50:14] really awesome to see like the whole
[00:50:16] company getting accelerated by codeex
[00:50:18] like from and you know most obviously
[00:50:21] also research and like improving how
[00:50:23] quickly we train models and how well we
[00:50:24] do it and then even like uh design as we
[00:50:27] talked about and and marketing like
[00:50:28] actually we're at this point now where
[00:50:30] uh my product marketer is often also
[00:50:32] making string changes just directly from
[00:50:34] Slack or like updating docs directly
[00:50:36] from Slack.
[00:50:37] >> These are amazing examples. You guys are
[00:50:39] living at the bleeding edge of what is
[00:50:42] possible and this is how other companies
[00:50:44] are going to work. Uh just shipping
[00:50:46] again what became the number one app in
[00:50:47] the app store and just beloved all over
[00:50:49] the it just like took over the I don't
[00:50:50] know the world for at least a week. Uh
[00:50:54] built you said in 28 days and like I
[00:50:56] don't know 10 days 18 days just to get
[00:50:58] like the core of it working.
[00:51:00] >> Yeah. So like 18 days we had a thing
[00:51:02] that employees were playing with and
[00:51:03] then 10 days later we were out.
[00:51:05] >> And you said just a couple engineers.
[00:51:07] >> Yeah.
[00:51:07] >> Two or three. Okay. And then Atlas you
[00:51:09] said was took a week to build.
[00:51:11] >> No, no, no. So Atlas, not the whole
[00:51:13] week, but Atlas was like a really meaty
[00:51:16] project.
[00:51:16] >> Yeah.
[00:51:17] >> Um and so I was talking to one of the
[00:51:18] engineers on Atlas um about like you
[00:51:20] know just how what they use codex for
[00:51:23] and it's basically like we use codex for
[00:51:24] absolutely everything. I was like okay
[00:51:25] well like you know how would you how
[00:51:27] would you measure the acceleration? And
[00:51:29] so basically the the answer I got back
[00:51:30] was
[00:51:31] >> previously it would have taken two to
[00:51:33] three weeks for two to three engineers
[00:51:34] and now it's like one engineer one week.
[00:51:36] Do you think this eventually moves to
[00:51:38] non-engineers doing this sort of thing?
[00:51:39] Like does it have to be an engineer
[00:51:41] building this thing? Could sort of have
[00:51:42] built been built by I don't know a PM or
[00:51:44] designer. I think we will very much get
[00:51:46] to the point where well basically where
[00:51:48] the boundaries are a little bit blurred,
[00:51:50] right? Like I think you're going to want
[00:51:52] someone who's like understands the
[00:51:54] details of what they're building, but
[00:51:55] what details those are will evolve. Kind
[00:51:58] of like how now like if you're writing
[00:51:59] Swift, you don't have to speak assembly.
[00:52:02] You know, there's a handful of people in
[00:52:04] the world and it's really important that
[00:52:05] they exist. and like speak assembly. Uh
[00:52:08] maybe more than a handful, right? But
[00:52:09] that's like a specialized function that
[00:52:10] like most companies don't need to have.
[00:52:14] So I think we're just going to naturally
[00:52:15] see like an increase in layers of
[00:52:17] abstraction. And then the cool thing is
[00:52:20] now we're entering like the language
[00:52:21] layer of abstraction like natural
[00:52:23] language. And then natural language
[00:52:25] itself is really flexible, right? Like
[00:52:27] you could have engineers talking about
[00:52:29] like a plan and then you could have
[00:52:30] engineers talking about a spec and then
[00:52:32] you could have engineers talking about
[00:52:33] just, you know, a product or an idea. So
[00:52:35] I think we can also like start moving up
[00:52:36] those layers of of abstraction as well.
[00:52:39] But you know I I do think this is going
[00:52:41] to be gradual. I don't think it's going
[00:52:43] to go to like all of a sudden like
[00:52:44] nobody ever writes anything and like you
[00:52:46] know any code and it's just specs. I
[00:52:47] think it's going to be much more like
[00:52:48] okay we've set up our coding agent to be
[00:52:51] really good at like previewing the build
[00:52:53] or like at running tests. Maybe that's
[00:52:54] the first part right that most people
[00:52:56] have set up. And it's like okay now
[00:52:57] we've set it up so that it can like
[00:52:59] execute the build and it can like see
[00:53:01] the results of its own changes but you
[00:53:03] know we haven't yet built a good
[00:53:04] integration harness so that it can like
[00:53:06] in the case of Atlas like by the way I
[00:53:07] don't know if they've done any of this
[00:53:08] or not I think they've done a lot of
[00:53:09] this but you know maybe the next stage
[00:53:11] is like enable it to like load a few
[00:53:14] sample pages to see how well those work
[00:53:16] right so then okay now we're going to
[00:53:17] like set up set up do that and I think
[00:53:19] for some time at least we're going to
[00:53:20] have humans kind of curating like which
[00:53:22] of these connectors or systems or
[00:53:24] components that the agent needs to be
[00:53:26] good at talking to and then you know in
[00:53:28] the future there will be an even greater
[00:53:30] unlock where Codex tells you how to set
[00:53:31] it up or maybe sets itself up in a repo.
[00:53:34] What a wild time to be alive. Wow. I'm
[00:53:37] curious just the second order effects of
[00:53:38] this sort of thing. Just how quickly it
[00:53:40] is to build stuff. What does that do?
[00:53:42] Does that mean distribution becomes much
[00:53:43] much more important? Does it mean uh
[00:53:46] ideas are just worth a lot more? It's
[00:53:48] interesting to think about how quick how
[00:53:50] that changes.
[00:53:51] >> I'm curious what you think. I still
[00:53:52] don't think ideas are worth as much as
[00:53:56] maybe some a lot of people think. I
[00:53:58] think still think execution is really
[00:53:59] hard, right? Like you can build
[00:54:00] something fast, but you still need to
[00:54:01] execute well on it. Still needs to make
[00:54:03] sense and be a coherent thing overall.
[00:54:06] Um Yeah. And distribution is massive.
[00:54:08] >> Yeah. Just feels like everything else is
[00:54:10] now more important. Everything that
[00:54:11] isn't the building piece, which is
[00:54:13] >> coming up with an idea, getting to
[00:54:15] market, profit,
[00:54:17] >> all that kind of stuff. I I think we
[00:54:19] might have been in this weird temporary
[00:54:21] phase where you know for a while like
[00:54:24] you could you could just it was so hard
[00:54:26] to build product that you mostly just
[00:54:30] had to be really good at building
[00:54:31] product and it maybe didn't matter if
[00:54:32] you like had an intimate understanding
[00:54:34] of a specific customer.
[00:54:37] Um, but now I think we're getting to
[00:54:39] this point where actually like if I
[00:54:40] could only choose like one thing to
[00:54:42] understand, it would be like really
[00:54:43] meaningful understanding of like the
[00:54:46] problems that a certain customer has,
[00:54:48] right? If I could only if I could only
[00:54:49] go in with one like core competency. So
[00:54:52] I think that that's that's ultimately
[00:54:54] still what's going to matter most,
[00:54:55] right? Like if you're starting a new
[00:54:57] company today and you have like a really
[00:55:00] good understanding and like network of
[00:55:02] customers that are currently underserved
[00:55:03] by AI tools, I think you're like you're
[00:55:05] set, right? Whereas if you're like good
[00:55:07] [clears throat] at building like you
[00:55:09] know websites, but you don't have any
[00:55:11] specific customer to build for, I think
[00:55:12] you're in for a much harder time.
[00:55:14] Bullish on vertical AI startups is what
[00:55:16] I'm hearing. Yeah, I completely agree.
[00:55:19] There's like, you know, there's like the
[00:55:20] general thing that can solve a lot of
[00:55:21] problems and then there's like we're
[00:55:22] going to solve presentations incredibly
[00:55:24] well and we're going to understand the
[00:55:25] presentation problem uh better than
[00:55:27] anyone and we're going to uh plug into
[00:55:30] your workflows and all these other
[00:55:32] things that matter for a very specific
[00:55:33] problem. Okay. Incredible. When you
[00:55:37] think about progress on codecs, I
[00:55:39] imagine you have a bunch of evals and
[00:55:40] there's all these public benchmarks.
[00:55:42] What's something you look at to tell
[00:55:44] you, okay, we're making really good
[00:55:45] progress. I imagine it's not going to be
[00:55:46] the one thing, but what do you focus on?
[00:55:48] What's like something you're trying to
[00:55:49] push? What's like a KPI or two? One of
[00:55:51] the things that I'm constantly reminding
[00:55:53] myself of is that a tool like Codex sort
[00:55:56] of naturally is a tool that you would,
[00:55:58] you know, become a power user of, right?
[00:56:00] And so we can accidentally spend a lot
[00:56:02] of our time thinking about features that
[00:56:03] are like very deep in the user adoption
[00:56:05] journey. Um, and so we can kind of end
[00:56:08] up oversolving for that. And so I think
[00:56:10] it's like just critically important to
[00:56:12] like go look at like your like D7
[00:56:13] retention, right? just go try the
[00:56:16] product. Like sign up from scratch
[00:56:17] again. Um I have a few too many like
[00:56:19] catchup pro accounts that I've just like
[00:56:22] in order to maximally correctly dog food
[00:56:24] like signed up for on my Gmail and they
[00:56:25] charge me like 200 bucks a month. I need
[00:56:27] to expense those. But uh uh you know
[00:56:30] like I think just like the feeling of
[00:56:33] being a user and the early retention
[00:56:35] stats are still like super important for
[00:56:37] us because you know as much as this
[00:56:39] category is is taking off I think we're
[00:56:41] still in the very early days of like
[00:56:42] people using them. Um, another thing
[00:56:45] that we do that that might might be I
[00:56:48] think we might be the most like user
[00:56:51] feedback slashsocial media pill team out
[00:56:54] there in this space is like a few of us
[00:56:56] are like constantly on Reddit and
[00:56:59] Twitter and uh you know there's a
[00:57:01] there's praise up there and there's a
[00:57:03] lot of complaints but we take the
[00:57:04] complaints like very seriously and look
[00:57:05] at them and I think that again because
[00:57:08] you can use like coding agent for so
[00:57:10] many different things um it often is
[00:57:12] like kind of broken in any sort of ways
[00:57:14] for like specific behaviors. Um, and so
[00:57:17] we we actually monitor a lot just like
[00:57:18] what the vibes are on social media
[00:57:20] pretty often, especially I think for for
[00:57:24] Twitter X, um, it's a little bit more
[00:57:27] hypy and then Reddit is a little more
[00:57:30] negative but real actually. Um, so I've
[00:57:34] started increasingly paying attention to
[00:57:36] like how people are talking about using
[00:57:37] Codex on Reddit. Actually,
[00:57:39] >> this is uh important for people to know.
[00:57:41] Which the subreddits do you check most?
[00:57:42] Is there like an R codeex or
[00:57:44] >> I mean the algorithm is pretty good at
[00:57:45] surfacing stuff but like r/codex is is
[00:57:48] there
[00:57:48] >> okay I'll take very interesting and then
[00:57:51] uh if people tag you on Twitter you
[00:57:52] still see that but maybe not as powerful
[00:57:54] as seeing it on Reddit.
[00:57:56] >> Well yeah the interesting well the thing
[00:57:57] with Twitter is it's a little bit more
[00:57:58] onetoone even if it's like in public
[00:58:00] whereas like with Reddit there's like
[00:58:01] really good upvoting mechanics and like
[00:58:03] maybe most people are still not bots
[00:58:05] unclear. Um so you get you get like good
[00:58:07] signal on what matters and what other
[00:58:08] people think. So uh interestingly uh
[00:58:11] Atlas I want to talk about that briefly.
[00:58:13] Uh you guys launched Atlas. I tweeted
[00:58:16] actually that I tried Atlas and then I I
[00:58:18] don't love the AI only uh search
[00:58:21] experience. I was just like I just want
[00:58:23] Google sometimes or whatever like just
[00:58:25] waiting for AI to give me an answer. I'm
[00:58:26] like I don't want to and there was no
[00:58:27] way to switch. I just tweeted hey I'm
[00:58:29] I'm switching back. I don't it's not
[00:58:31] great. And I feel like I made some PMs
[00:58:32] at OpenAI sad and I saw someone tweet
[00:58:35] okay we have this now which I imagine
[00:58:36] was always part of the plan. It's
[00:58:38] probably an example of we just ship we
[00:58:40] got to ship stuff, see how people use it
[00:58:41] and then we figure it out. Uh so I guess
[00:58:43] one is that I don't know is there
[00:58:45] anything there and two I'm just curious
[00:58:46] why are you guys building a web browser?
[00:58:48] So I I worked on Atlas for a bit. Um I
[00:58:50] don't work on it now. Um but you know
[00:58:54] like the a bit of the narrative here for
[00:58:55] for me just to tell my story a bit was
[00:58:57] like I was working on this like screen
[00:58:58] sharing like pair programming startup
[00:59:01] right and then we joined open AI and so
[00:59:03] the idea was really to build a
[00:59:04] contextual desktop assistant and the
[00:59:07] reason I believe that's so important is
[00:59:08] because I think that it's really
[00:59:11] annoying to have to give all your
[00:59:12] context to an assistant and then to
[00:59:14] figure out how it can help you right and
[00:59:16] so if it could just like understand what
[00:59:18] you are trying to do then it could
[00:59:19] maximally accelerate do um and so I I I
[00:59:23] would you know I still think of Codex
[00:59:24] actually as like a contextual assistant
[00:59:26] um from a little bit of a different
[00:59:28] angle like starting with coding tasks
[00:59:30] but um the some of the some of the
[00:59:34] thinking at least for me personally I
[00:59:36] can't speak for the whole project but
[00:59:37] was that a lot of work is done in the
[00:59:40] web and if we could build a browser then
[00:59:43] we could be contextual for you but in a
[00:59:45] much more first class way we weren't
[00:59:47] hacking like other desktop software
[00:59:48] which have like very varied report for
[00:59:51] for like what content they're rendering
[00:59:52] to the accessibility tree. Uh we
[00:59:54] wouldn't be relying on screenshots which
[00:59:56] are a little bit slower and unreliable.
[00:59:58] Instead, we we could like be in the
[01:00:00] rendering engine, right? And like
[01:00:01] extract whatever we needed to to help
[01:00:03] you. Um and also I like to think of like
[01:00:07] you know video games like I don't know
[01:00:09] if you've played like I don't know say
[01:00:10] Halo right like you walk up to an
[01:00:13] object. I mean this true for many games
[01:00:14] you press man it's been a long time this
[01:00:16] is embarrassing. press X and it just
[01:00:19] does the right thing, right? And I was
[01:00:21] one of those guys who always read the
[01:00:22] instruction manual for every video game
[01:00:23] that I bought. And I remember the first
[01:00:25] time I read about a contextual action
[01:00:26] and I just thought it was like this
[01:00:27] really cool idea. And uh you know the
[01:00:31] the thing about a contextual action is
[01:00:33] we need to know what you are attempting
[01:00:34] to do. We need to have a little bit of
[01:00:35] context and then we can and then we can
[01:00:37] help. Uh, and I think this is critically
[01:00:40] important because you know, imagine this
[01:00:42] world that we reach, right, where we're
[01:00:44] we have agents that are helping you
[01:00:45] thousands of times per day. Um, imagine
[01:00:49] if the only way we could tell you that
[01:00:50] we helped you is if we could like push
[01:00:52] notify you. So, you get a thousand push
[01:00:55] notifications a day of an AI saying
[01:00:57] like, "Hey, I did this thing. Do you
[01:00:59] like it?" It'd be super annoying, right?
[01:01:01] Whereas imagine going back to software
[01:01:03] engineering like I was looking at a
[01:01:05] dashboard and I noticed some like key
[01:01:07] metric had like gone down
[01:01:09] and you know at that point in time an II
[01:01:12] could like maybe go take a look and then
[01:01:13] surface the fact that it has an opinion
[01:01:15] on why this metric went down and maybe a
[01:01:17] fix right there right when I'm looking
[01:01:18] at the dashboard right that would be
[01:01:20] like that would much more keep me in
[01:01:22] flow and enable the agent to take action
[01:01:25] on like many more things so in my mind
[01:01:27] like part of why I'm excited for us to
[01:01:29] have a browser is that I think we have
[01:01:32] then like much more context around like
[01:01:35] what we should help with. Users have
[01:01:37] much more control over what they want us
[01:01:39] to look at. It's like hey if you want to
[01:01:40] open if you want us to like take action
[01:01:42] on something you can open it in your AI
[01:01:43] browser. If you don't then you can open
[01:01:44] it in your other browser right? So like
[01:01:46] really clear control and boundaries and
[01:01:48] then we have the ability to build UX
[01:01:50] that's like mixed initiative so that we
[01:01:53] can surface contextual actions to you
[01:01:54] like at the times they're helpful as
[01:01:56] opposed to just like randomly notifying
[01:01:58] you. hearing the vision for Codeex being
[01:01:59] the super assistant. It's not just there
[01:02:01] to code for you. It's trying to do a lot
[01:02:03] for you as a teammate, as this kind of
[01:02:05] super teammate that makes you awesome at
[01:02:07] work. So, I get this. Speaking of that,
[01:02:10] are there other non-engineering
[01:02:13] common use cases for codecs? Just ways
[01:02:15] that non-engineers, we talked about it,
[01:02:17] you know, designers prototyping and
[01:02:18] building stuff. Are there any, I don't
[01:02:20] know, fun or unexpected ways people are
[01:02:22] using codecs that aren't engineers? I
[01:02:24] mean there's a load of a load of
[01:02:25] unexpected ways but I think like most of
[01:02:29] where we're seeing like real traction
[01:02:30] with people using things are still for
[01:02:32] now like very like I would say coding
[01:02:35] adjacent or like sort of tech oriented
[01:02:38] places where there's like a mature
[01:02:39] ecosystem um or you know maybe you're
[01:02:41] doing data an data analysis or something
[01:02:43] like that. I personally am expecting
[01:02:46] that we're going to see a lot more of
[01:02:47] that over time. Um, but for now like
[01:02:50] we're keeping the team like very focused
[01:02:51] on just coding for now because there's
[01:02:52] so much more work to do.
[01:02:54] >> For people that are thinking about
[01:02:55] trying out codecs, is there like um does
[01:02:58] it work for all kinds of code bases?
[01:03:00] What what code does it support? If
[01:03:02] you're like I don't know SAP, can you
[01:03:04] add codec and start building things?
[01:03:06] What's kind of like the sweet spot or
[01:03:08] does it start to not be amazing yet?
[01:03:11] This I'm really glad you asked this
[01:03:12] question actually because the best way
[01:03:14] to try codeex is to give it your hardest
[01:03:16] tasks which is a little different than
[01:03:19] some of the other coding agents like you
[01:03:21] know some tools you might think okay let
[01:03:23] me like start easy or just like you know
[01:03:25] like vibe code something random and
[01:03:27] decide if I like the tool whereas like
[01:03:30] we're really building codeex to be the
[01:03:32] like professional tool that you can give
[01:03:33] your like hardest problems to um and you
[01:03:36] know that writes like high quality code
[01:03:38] in your like enormous code base that is
[01:03:40] in fact not perfect right now. So yeah,
[01:03:42] I think if you're going to try codeex,
[01:03:43] you want to try it on like a real task
[01:03:46] that you have and not necessarily like
[01:03:48] dumb that task down to something that's
[01:03:50] like trivial, but actually like you know
[01:03:52] like a good one would be like you have a
[01:03:54] hard bug and you don't know what what's
[01:03:55] causing that bug and you ask Codex to
[01:03:57] like help figure that out or like to
[01:03:59] implement that, you know, the fix.
[01:04:00] >> I love that answer. Just give it your
[01:04:02] hardest problem. I will say like you
[01:04:03] know if you if you're like hey okay well
[01:04:05] the hardest problem I have is that I
[01:04:06] need to build like a new unicorn
[01:04:08] business like obviously that you know
[01:04:10] it's not going to work not yet. So I
[01:04:13] think it's like give it like the hardest
[01:04:16] problem but something that is still like
[01:04:18] one like question right or one task um
[01:04:21] to start that's if you're testing and
[01:04:23] then over time you can learn how to use
[01:04:24] it for like bigger things.
[01:04:25] >> Yeah. What languages does does it
[01:04:27] support? Basically the way we've trained
[01:04:28] codeex is like there's a distribution of
[01:04:30] languages that we support and it's like
[01:04:32] fairly aligned with like the frequency
[01:04:34] of these languages in the world. So
[01:04:36] unless you're writing some like very
[01:04:37] esoteric language or like some private
[01:04:39] language, it should do fine in your
[01:04:40] language. If someone was just getting
[01:04:42] started, is there a tip you could share
[01:04:44] to help them be successful? Like if you
[01:04:46] could just whisper a little tip into
[01:04:48] someone just setting up Codex for the
[01:04:49] first time to help them have a really
[01:04:51] good time, what's something you would
[01:04:52] whisper?
[01:04:53] >> I might say try a few things in
[01:04:55] parallel, right? Right? So you could try
[01:04:57] giving it a hard task. Um maybe ask it
[01:05:00] to understand the codebase. Uh formulate
[01:05:03] a plan with it around an idea that you
[01:05:05] have and kind of build your way up from
[01:05:07] there. And like sort of the meta idea
[01:05:09] here is it's again it's like you're
[01:05:11] building trust with the new teammate,
[01:05:13] right? And so like you wouldn't go to a
[01:05:15] new teammate and just give them like hey
[01:05:16] do this thing here's zero context. you
[01:05:18] would start by like first making sure
[01:05:19] they understand the codebase and then
[01:05:22] you would like maybe align on a an
[01:05:23] approach and then you would have them go
[01:05:24] off and do bit by bit right and I think
[01:05:26] if you use codeex in that way you'll
[01:05:28] just sort of naturally start to
[01:05:29] understand like the different ways of
[01:05:30] prompting it because it is it's a super
[01:05:32] powerful like agent and model but it is
[01:05:35] it is a little bit different to prompt
[01:05:36] codeex and other models just a couple
[01:05:38] more questions one we touch on this a
[01:05:41] little bit as AI does more and more
[01:05:44] coding there's always this question of
[01:05:46] should I learn to code why should they
[01:05:48] spend time doing this sort of thing. For
[01:05:50] people that are trying to figure out
[01:05:52] what to do with their career, especially
[01:05:53] if they're into software engineering,
[01:05:55] computer science, do you think there's
[01:05:57] specific elements of computer science
[01:05:58] that are mo more and more important to
[01:06:01] lean into maybe things they don't need
[01:06:03] to worry about? Like what do you think
[01:06:04] people should be leaning into skill-wise
[01:06:06] in as this becomes more and more of a
[01:06:09] thing in our workplace? I think there's
[01:06:11] like a couple angles you could go at
[01:06:14] this from. Um, I think the,
[01:06:18] well, the easiest one to think of at
[01:06:20] least is just like be a doer of things.
[01:06:24] Um, I think that, you know, with coding
[01:06:26] agents, um, getting better and better
[01:06:28] over time. It's just what you can do as
[01:06:31] even like someone in college or a new
[01:06:33] grad is just like so much more than what
[01:06:35] that was before. And so, I think you
[01:06:37] just want to be taking advantage of
[01:06:38] that. You know, definitely when I'm
[01:06:40] looking at like hiring folks who are
[01:06:42] earlier career, it's like definitely
[01:06:43] something that I think about is how how
[01:06:46] productive are they using the latest
[01:06:47] tools, right? They should be like super
[01:06:49] productive. And if you think of it in
[01:06:51] that way, they actually have like less
[01:06:52] of a handicap than before versus a more
[01:06:55] senior career person because, you know,
[01:06:57] the divide is actually getting smaller
[01:06:59] because they've got these amazing coding
[01:07:00] agents now. Um, so that's one thing
[01:07:02] which is like I guess the thing the
[01:07:03] advice is just like learn about whatever
[01:07:05] you want but just make sure you spend
[01:07:07] time doing things not just like
[01:07:08] fulfilling homework assignments. I guess
[01:07:11] I think the other side of it though is
[01:07:12] that it's still deeply worth
[01:07:15] understanding like what makes a good
[01:07:17] like overall software system. So I still
[01:07:20] think that like skills like really
[01:07:22] strong systems engineering skills or
[01:07:25] even like really effective like
[01:07:27] communication and collaboration with
[01:07:29] your team, skills like that I think are
[01:07:31] are important are going to continue to
[01:07:32] matter for for quite some time. Like I
[01:07:35] don't think it's going to be like all of
[01:07:36] a sudden uh the AI coding agents are
[01:07:39] just able to build like perfect systems
[01:07:41] without your help. I think it's going to
[01:07:43] look much more gradual where it's like
[01:07:46] okay we have these AI coding agents
[01:07:48] they're able to validate their work it's
[01:07:50] still important and like for example
[01:07:52] like I'm thinking of an engineer who was
[01:07:54] working on Atlas since we were talking
[01:07:55] about it he set up codeex so it can like
[01:07:57] verify its own work which is a little
[01:07:59] bit non-trivial because of the nature of
[01:08:00] the Atlas project. So the way that he
[01:08:02] did that was he actually prompted codeex
[01:08:03] like hey why can't you verify your work
[01:08:05] fix it and like did that on a loop right
[01:08:08] and so you still like at various phases
[01:08:11] are going to want a human in the loop to
[01:08:13] like help configure the coding agent to
[01:08:15] be effective and so I think like you
[01:08:17] still want to be able to reason about
[01:08:19] that so maybe it's like less important
[01:08:20] that you can like type really fast and
[01:08:23] like you understand exactly how to write
[01:08:25] not that anyone writes a you know for
[01:08:26] each loop or something right but it is
[01:08:30] or you know you don't need to know how
[01:08:31] implement like a specific algorithm. But
[01:08:32] I think you need to be able to reason
[01:08:33] about the different systems and like
[01:08:34] what makes like effective a software
[01:08:36] engineering team effective. So I think
[01:08:38] that's the other really important thing.
[01:08:40] And then like maybe the last angle that
[01:08:41] you could take is I think if you're on
[01:08:44] the frontier of knowledge for a given
[01:08:46] thing, I still think that's like deeply
[01:08:49] interesting to go down partially because
[01:08:51] that knowledge is still going to be like
[01:08:54] uh you know agents aren't going to be as
[01:08:56] good at that. But also partially because
[01:08:58] I think that like by trying to advance
[01:08:59] the frontier of a specific thing, you'll
[01:09:01] actually like end up like being forced
[01:09:03] to take advantage of coding agents and
[01:09:05] like using them to accelerate your own
[01:09:08] workflow as you go.
[01:09:09] >> What's an example that when you when you
[01:09:10] talk about being at the frontier? So
[01:09:12] >> Codex writes a lot of the code that
[01:09:13] helps like manage its training runs, the
[01:09:15] key infrastructure. Uh you know, we move
[01:09:18] pretty fast and so we have a Codex code
[01:09:21] review is like catching a lot of
[01:09:22] mistakes. It's actually caught some like
[01:09:23] pretty interesting configuration
[01:09:25] mistakes and uh you know we're starting
[01:09:27] to see glimpses of the future where
[01:09:29] we're actually starting to have codeex
[01:09:31] even like be on call for its own
[01:09:33] training which is pretty interesting. Um
[01:09:36] so there's lots there.
[01:09:37] >> Uh wait what does that mean to be on
[01:09:39] call for its own training? So it's
[01:09:40] running it's training and it's like oh
[01:09:42] something broke someone needs and it it
[01:09:44] does it like alert people or it's like
[01:09:45] here I'm going to fix the problem and re
[01:09:46] restart. This is an early idea that
[01:09:48] we're like figuring out, but the basic
[01:09:50] idea is that you know during a training
[01:09:51] run there's like a bunch of graphs that
[01:09:53] like today like humans are looking at
[01:09:54] and it's like really important to like
[01:09:56] look at those. Um we call this
[01:09:58] babysitting
[01:09:59] >> because it's very expensive to train I
[01:10:00] imagine and very important to move fast
[01:10:02] and exactly and there's a lot of there's
[01:10:04] a lot of systems underlying uh the
[01:10:06] training run and so like a system could
[01:10:08] go down or there could be an error
[01:10:09] somewhere that gets introduced and so we
[01:10:11] might need to like fix it or pause
[01:10:13] things or I don't know there's lots of
[01:10:14] actions we might need to take and so
[01:10:16] basically having codeex like run on a
[01:10:18] loop to like evaluate how those charts
[01:10:20] are moving over time um is sort of this
[01:10:22] idea that we have to like how to enable
[01:10:24] us to like train like way more
[01:10:25] efficiently. I love that. This is very
[01:10:27] much along the lines of this is the
[01:10:29] future of agents. It's codeex isn't just
[01:10:31] for building code, right? It's it's a
[01:10:33] lot more than that.
[01:10:34] >> Yeah.
[01:10:36] >> Okay. Last question. Uh being at OpenAI,
[01:10:39] uh I can't not ask about your AGI
[01:10:41] timeline and how far you think we are
[01:10:43] from AGI. I know this isn't what you
[01:10:45] work on, but there's a lot of opinions,
[01:10:47] a lot of I don't know timelines. How far
[01:10:50] do you think we are from a humanly human
[01:10:54] version of AI? Whatever that means to
[01:10:56] you. For me, I think that it's a little
[01:10:59] bit about like when do we see the
[01:11:01] acceleration curves kind of go like this
[01:11:02] or I don't know which way I'm mirrored
[01:11:03] here, right? When do we see the hockey
[01:11:05] stick? And I think that the current
[01:11:08] limiting factor, I mean there's many,
[01:11:10] but I think a current underappreciated
[01:11:11] limiting factor is like literally human
[01:11:13] typing speed or human multitasking speed
[01:11:16] on like writing prompts,
[01:11:19] right? And like you know, you were
[01:11:20] talking about it's like you can have an
[01:11:21] agent like watch all the work you're
[01:11:22] doing, but if you don't have the agent
[01:11:24] uh also validating its work, then you're
[01:11:27] still bottlenecked on like can you go
[01:11:28] review all that code, right? So my view
[01:11:30] is that we need to um unblock those
[01:11:35] productivity loops from like humans
[01:11:36] having to prompt and humans having to
[01:11:38] like manually validate all the work. And
[01:11:40] so if we can like rebuild systems to let
[01:11:42] the agent like be default useful, we'll
[01:11:45] start unlocking hockey sticks.
[01:11:47] Unfortunately, I don't think that's
[01:11:48] going to be binary. I think it's going
[01:11:49] to be very dependent on what you're
[01:11:51] building, right? So like I would imagine
[01:11:52] that like next year if you're a startup
[01:11:55] and you're building a new new piece of
[01:11:57] like you know some new app or something
[01:11:59] it'll be possible for you to set it up
[01:12:00] on a stack where agents are like much
[01:12:02] more self sufficient than not right but
[01:12:05] now let's say I don't know you message
[01:12:07] SAP right let's say you work in SAP like
[01:12:09] they have many like complex systems and
[01:12:11] they're not going to be able to just
[01:12:12] like get the agent to be self-sufficient
[01:12:13] overnight in those systems so they're
[01:12:15] going to have to slowly like maybe
[01:12:16] replace systems or update systems to
[01:12:19] allow the agent to like handle more of
[01:12:21] the work end to end. And so basically my
[01:12:24] sort of long answer to your question,
[01:12:25] maybe boring answer is that I think
[01:12:27] starting next year we're going to see
[01:12:28] like early adopters like starting to
[01:12:30] like hockey stick their productivity. Um
[01:12:33] and then over the years that follow,
[01:12:34] we're going to see larger and larger
[01:12:36] companies like hockey stick that
[01:12:37] productivity. And then somewhere in that
[01:12:39] fuzzy middle is like when that hockey
[01:12:42] sticking will be like flowing back into
[01:12:44] the AI labs and that's when we'll we'll
[01:12:46] basically be at the AGI tier.
[01:12:48] >> I love this answer. It's very practical
[01:12:50] and it's something that comes up a lot
[01:12:52] on this podcast just like the time to
[01:12:54] review all the things AI is doing is
[01:12:55] really annoying and a big bottleneck. I
[01:12:58] love that you're working on this because
[01:12:59] it's one thing to just make coding much
[01:13:01] more efficient and do that for people.
[01:13:03] It's another to take care of that final
[01:13:05] step of okay is this actually great? And
[01:13:08] that's so interesting that your sense is
[01:13:09] that's the limiting factor. It comes
[01:13:11] back to your earlier point of even if AI
[01:13:14] did not advance anymore. We have so much
[01:13:16] more potential to unlock if we uh as we
[01:13:20] learn to use it more effectively. Uh so
[01:13:22] that is a really unique answer. I
[01:13:24] haven't heard that perspective on what
[01:13:25] is the big unlock human typing speed to
[01:13:27] review basically what AI is doing for
[01:13:29] us.
[01:13:30] >> Mhm. So good. Okay. Uh Alexander, we
[01:13:33] covered a lot of ground. Is there
[01:13:35] anything that we haven't covered? Is
[01:13:37] there anything you wanted to share,
[01:13:38] maybe double down on before we get to
[01:13:41] our very exciting lightning round? I
[01:13:44] think uh one thing is that the codeex
[01:13:45] team is growing and uh as I was just
[01:13:48] saying, we're still somewhat limited by
[01:13:50] human thinking speed and human typing
[01:13:51] speed. We're working on it. So um if
[01:13:54] you're an engineer um or a salesperson
[01:13:58] or I am hiring for product, a product
[01:14:00] person, uh please hit us up. I'm not
[01:14:02] sure the best way to give contact info,
[01:14:04] but I guess you can go to our jobs page
[01:14:06] or do they have contact for you?
[01:14:08] Actually, do listeners have contact for
[01:14:10] you
[01:14:10] >> before they send me like, "Hey, I want
[01:14:11] to apply to Codex."
[01:14:13] >> Uh, I do have a contact form at lenny
[01:14:15] richchi.com. I'm afraid of all the
[01:14:16] amazing people that are ping me. But
[01:14:18] there we go. We could try that. Let's
[01:14:19] see how that goes.
[01:14:20] >> Okay. Or Yeah. Or another maybe an
[01:14:21] easier. We can edit all that out or up
[01:14:24] to you. But uh yeah, or I would just say
[01:14:26] you can drop us a DM. Uh, for example,
[01:14:28] I'm Emir Rico on Twitter and hit me up
[01:14:31] if you're interested in joining the
[01:14:32] team.
[01:14:33] >> What a dream job for so many people.
[01:14:35] What's a sign they I don't know what's
[01:14:38] like a way to filter people a little bit
[01:14:40] so they're not flooding your inbox.
[01:14:42] >> So, specifically, if you want to join
[01:14:44] the codeex team, then you need to be a
[01:14:46] technical person who uses these tools.
[01:14:49] And I think I would just ask yourself
[01:14:50] the question, uh, hey, let's say, you
[01:14:52] know, I were to join OpenAI and work on
[01:14:54] Codeex over the next six months, you
[01:14:57] know, and crush it. What does the life
[01:14:59] of a software engineer look like then?
[01:15:01] And I think if you have an opinion on
[01:15:02] that, you should apply. And if you don't
[01:15:04] have an opinion on that and have to
[01:15:05] think about it first, you know,
[01:15:08] depending on how long you have to think
[01:15:09] about it, I guess that would be the
[01:15:10] filter, right? Like I think there's a
[01:15:12] lot of people thinking about the space
[01:15:13] and so we're we're very interested in
[01:15:16] folks who sort of have already been
[01:15:19] thinking about like what the future
[01:15:21] should look like with agents and like we
[01:15:22] don't have to agree on where where we're
[01:15:23] going but I think we want people who
[01:15:25] like are very passionate about the
[01:15:26] topic. I guess
[01:15:28] >> it's very rare to be working on a
[01:15:30] product that has this much impact and is
[01:15:32] at such a bleeding edge of where it's
[01:15:34] possible. It's uh what a cool role for
[01:15:37] the right person. So, uh, um, it's
[01:15:38] awesome that you have an opening and
[01:15:40] this audience is, uh, a really good fit
[01:15:43] potentially for for that role. So, I
[01:15:45] hope we find someone that would be
[01:15:46] incredible. With that, we've reached our
[01:15:49] very exciting lightning round. I've got
[01:15:51] five questions for you, Alexander. Are
[01:15:53] you ready?
[01:15:54] >> I don't know what these are, but I'm
[01:15:55] excited. Let's do it.
[01:15:57] >> Uh, they're uh, the same questions ask
[01:15:59] everyone except for the last one. So,
[01:16:02] uh, probably not a surprise. I should
[01:16:04] probably make them more more often a
[01:16:06] surprise. Okay, first question. What are
[01:16:08] a couple books that you recommend most
[01:16:09] to other people? Two or three books that
[01:16:11] come to mind. I have been reading a lot
[01:16:14] of science fiction recently. And I'm
[01:16:16] sure this has been recommended before,
[01:16:18] but The Culture,
[01:16:20] I think it's Ian Banks is the name of
[01:16:22] the author. Part of why I love it is
[01:16:24] because it's like basically relatively
[01:16:27] recent writing about a future with AI,
[01:16:30] but it's an optimistic future with AI.
[01:16:33] Um, and I think, you know, a lot of
[01:16:34] sci-fi is like fairly dystopian. Um, but
[01:16:37] this is like people uh sort of the joke
[01:16:39] at least on the sub culture subreddit is
[01:16:42] that let me let me see if I can get this
[01:16:43] right. It is a like space communist
[01:16:46] utopia or or like I think it's a gay
[01:16:49] space communist utopia. Um, and uh I
[01:16:53] just think it's like really fun to think
[01:16:54] about um like to use the culture as a
[01:16:57] way to think about like what kind of
[01:16:58] world can we usher in and like what
[01:16:59] decisions can we make today to help
[01:17:01] usher in that world.
[01:17:02] >> Wow. I've not I don't think anyone's
[01:17:03] recommended that. I know you're reading,
[01:17:05] you mentioned before I started recording
[01:17:06] Lord of the Rings right now. Uh if you
[01:17:09] want another AIish sci-fi book, uh have
[01:17:12] you read Fire Upon the Deep?
[01:17:14] >> No, I haven't.
[01:17:15] >> Okay. It's uh incredibly good. It's like
[01:17:18] a a sci-fi space opera sort of epic tale
[01:17:22] with uh super intelligence.
[01:17:24] >> Cool.
[01:17:25] >> Yeah. Somewhat mostly not optimistic,
[01:17:28] but somewhat optimistic. Okay. Next
[01:17:30] question. Is there a favorite recent
[01:17:33] movie or TV show that you've really
[01:17:35] enjoyed?
[01:17:36] >> Yeah, there's an anime called Jiu-Jitsu
[01:17:37] Kaisen, which I really like. Um, again,
[01:17:41] it's got a kind of a slightly dark topic
[01:17:43] of like demons. Um, but what I love
[01:17:46] about it is that the hero is really
[01:17:48] nice. And I think there's this new wave
[01:17:49] of like anime and cartoons where the
[01:17:52] protagonists are
[01:17:55] really friendly and like people who care
[01:17:57] about the world rather than being like
[01:17:59] sort of like if you look at like some
[01:18:01] older anime like that started the genre
[01:18:03] like you know those like Evangelian
[01:18:07] or Akita and like those characters the
[01:18:09] protagonists are like deeply flawed like
[01:18:11] quite unhappy
[01:18:13] um that they didn't start the genre but
[01:18:15] it was like a trend for a while to sort
[01:18:17] of poke poke fun at the idea that in
[01:18:19] these in these cartoons the protagonist
[01:18:21] was very young but being given a
[01:18:23] ridiculous amount of responsibility to
[01:18:24] like save the world. And so there was
[01:18:26] kind of a wave of like uh content that
[01:18:30] was like critiquing this by making the
[01:18:31] character like basically go through like
[01:18:33] serious like mental issues in the middle
[01:18:35] of the show. Um and I'm not saying this
[01:18:37] is better, but at least it's quite fun
[01:18:39] to have like these like really positive
[01:18:40] protagonists who are just trying to help
[01:18:42] everyone around them. I love how much
[01:18:44] we're learning about your uh personality
[01:18:46] during these recommendations.
[01:18:49] Nice protagonists, optimistic futures.
[01:18:52] >> I think, you know, if you don't believe
[01:18:53] it, you can't r will it into existence.
[01:18:55] So, you're in a balance.
[01:18:57] >> This is your training data.
[01:18:59] >> Is there a product you've recently
[01:19:01] discovered you really love? Could be an
[01:19:03] app, could be some clothing, could be
[01:19:05] some kitchen gadget, tech gadget, a hat.
[01:19:09] Yeah. So I have been like quite into uh
[01:19:13] you know combustion engines um and cars.
[01:19:17] Actually the reason I came to America
[01:19:19] initially was cuz I wanted to work on
[01:19:20] like US aircraft. Um but you know now I
[01:19:23] work in software. Um and so for the
[01:19:26] longest time I basically only had like
[01:19:28] quite old sports cars. Uh old just
[01:19:30] because they were more affordable. Um
[01:19:33] and then uh recently um we got a Tesla
[01:19:37] instead.
[01:19:38] And I have to say that I find the Tesla
[01:19:41] software like quite inspiring. Um, in
[01:19:43] particular, it has like the self-driving
[01:19:45] feature. And you know, I've mentioned a
[01:19:47] few times like today like I think it's
[01:19:49] really interesting to think about how to
[01:19:51] build like mixed initiative software
[01:19:52] that makes you feel maximally empowered
[01:19:54] as a human, maximally in control, but
[01:19:56] yet you're getting a lot of help. And I
[01:19:58] think they did a really good job with
[01:20:01] enabling sort of the car to drive
[01:20:03] itself, but all these different ways
[01:20:05] that you can adjust what it's doing
[01:20:06] without turning off the self-driving. So
[01:20:08] like you can accelerate, you know, it'll
[01:20:10] like listen to that, you can turn a knob
[01:20:12] to change its speed, you can steer
[01:20:14] slightly. Um, I think it's it's actually
[01:20:16] a masterass in like building an agent
[01:20:19] that still leaves the human in control.
[01:20:21] This reminds me Nick Turley's whole uh
[01:20:23] mantra was are we maximally accelerated?
[01:20:25] >> Yeah. Yeah,
[01:20:26] >> feels like it's completely infiltrated
[01:20:28] everything at OpenAI, which makes sense.
[01:20:30] That tracks. Uh, two more questions. Do
[01:20:33] you have a life motto that you often
[01:20:36] think about and come back to in work or
[01:20:38] in life that's been helpful?
[01:20:39] >> I don't know if I have a life motto, but
[01:20:41] maybe I can tell you about the number
[01:20:42] one value, company value from my
[01:20:45] startup.
[01:20:45] >> Love it.
[01:20:46] >> Which is still something that sticks
[01:20:47] with me, which is to be kind and candid.
[01:20:51] >> That tracks
[01:20:53] kind and candid. Wow. Yeah. And we had
[01:20:55] to put them together because we as
[01:20:58] founders realized that we often would be
[01:21:02] nice
[01:21:04] and it wasn't actually the right thing
[01:21:06] to do. We would like delay the difficult
[01:21:09] conversations and we were not candid.
[01:21:11] And so every time we would like remind
[01:21:12] ourselves of this motto and then we
[01:21:14] would become more candid and then six
[01:21:15] months later we would realize that we
[01:21:16] were in fact not candid six months ago
[01:21:18] and we needed to be even more candid. So
[01:21:20] then the question is like okay like how
[01:21:23] how should we be candid? It's like okay
[01:21:24] well let's let's think of being candid
[01:21:26] as an act of kindness but also think of
[01:21:28] that both in terms of doing it and
[01:21:29] willing ourselves to do it but also in
[01:21:31] terms of how we frame it to people.
[01:21:32] >> That is a beautiful uh way of
[01:21:35] summarizing how to how to lead well.
[01:21:36] What's the uh the book about dare uh
[01:21:39] challenge directly but care deeply uh
[01:21:42] radical cander.
[01:21:43] >> Oh yeah yeah
[01:21:44] >> yeah. So it's like another way of
[01:21:45] thinking about radical cander. Okay last
[01:21:47] question. I was looking up your last
[01:21:48] name just like hey what's the what's the
[01:21:50] story here? So your last name is
[01:21:52] Emiricos and I was talking at JGPT and
[01:21:55] it told me the most famous individuals
[01:21:57] with the surname are the influential
[01:22:00] Greek poet and psychoanalyst Andreas
[01:22:02] Emiros
[01:22:04] and his relative the wealthy shipping
[01:22:06] magnate and art collector George Mureos.
[01:22:09] So the question is which of these two do
[01:22:11] you most identify with? The Greek poet
[01:22:14] and psychoanalyst or the wealthy
[01:22:16] shipping magnate and art collector? I
[01:22:19] think it's it's gonna have to be the
[01:22:20] poet because uh he uh he loved the
[01:22:25] island that our family's from.
[01:22:26] >> Wait, you know those people? Okay, this
[01:22:29] is not news to you. Okay.
[01:22:30] >> Well, I mean it's an enormous family,
[01:22:32] but it's like Greek, so you know these
[01:22:34] big families, everyone like everyone's
[01:22:35] your uncle, you know what I mean? Like
[01:22:37] my mother's Malaysian and also like
[01:22:38] everyone is my uncle or aunt in
[01:22:40] Malaysia, too, if that makes sense.
[01:22:42] >> Yeah. But yeah, he he loved this island
[01:22:45] that the family sort of like initiated
[01:22:48] from. I believe I don't actually know
[01:22:50] where that chipping magnate lived. I
[01:22:51] think it was New York or something. But
[01:22:53] anyway, we all came from this island
[01:22:54] called Andros. Um, which is a really
[01:22:57] beautiful place and it's like there's
[01:22:58] more like livestock there than than
[01:23:00] humans. Uh, not too many tourists go
[01:23:03] there. Uh, but I think he like part of
[01:23:06] what I think is really cool is like he
[01:23:07] published a lot and a lot of his writing
[01:23:09] is about like the beauty of that island
[01:23:11] which I think is super cool.
[01:23:12] >> Wow, that was an amazing answer. Two
[01:23:14] more questions. Where can folks find you
[01:23:16] if they want to follow you online and
[01:23:17] you know maybe reach out and then how
[01:23:18] can listeners be useful to you?
[01:23:20] >> I I'm one of those people who has social
[01:23:22] media only for the purposes of having
[01:23:23] work. You know my phone my phone turns
[01:23:25] black and white at like 9:00 p.m. at
[01:23:27] night. Uh but yeah, so Twitter or XM
[01:23:30] Rico. Um, and uh, yeah, if you post in
[01:23:34] r/codeex, I'll probably see it. Uh, so
[01:23:37] you know, you can go there. Um, how can
[01:23:40] listeners be useful? Um, I would say
[01:23:42] please try codeex. Please share
[01:23:44] feedback. Let us know what to improve.
[01:23:46] We pay a ton of ton of attention to
[01:23:48] feedback. I think it's like honestly
[01:23:50] like the growth has been amazing, but
[01:23:51] it's still very early times. Um, so we
[01:23:54] still pay a lot of attention and hope to
[01:23:56] do so forever. Um and also um I would
[01:23:59] say if you're interested in working on
[01:24:01] the future of coding agents and then
[01:24:03] agents generally then please uh apply to
[01:24:06] our job site um and or message me in
[01:24:08] those social media places. Alexander
[01:24:11] this was awesome. I always love meeting
[01:24:12] people working on AI because it always
[01:24:15] feels like this very I don't know
[01:24:17] sterile scary mysterious thing and then
[01:24:20] you meet the people building these tools
[01:24:22] and they're always just so awesome and
[01:24:24] you especially just so nice and uh as
[01:24:28] you like the examples you shared
[01:24:30] optimism and kindness you know this is
[01:24:32] what we want to be this is these are the
[01:24:34] kinds of people we want to be building
[01:24:35] these tools that are going to drive the
[01:24:37] future so um I'm I'm really thankful
[01:24:39] that you did this Um, grateful to have
[01:24:42] met you and uh, thank you so much for
[01:24:44] being here.
[01:24:45] >> Yeah, thanks so much for having me. This
[01:24:46] is fun.
[01:24:48] Thank you so much for listening. If you
[01:24:50] found this valuable, you can subscribe
[01:24:51] to the show on Apple Podcasts, Spotify,
[01:24:54] or your favorite podcast app. Also,
[01:24:56] please consider giving us a rating or
[01:24:58] leaving a review as that really helps
[01:25:00] other listeners find the podcast. You
[01:25:03] can find all past episodes or learn more
[01:25:05] about the show at lennispodcast.com.
[01:25:08] See you in the next episode.
