[00:00:00] At the beginning of my day, I literally
[00:00:02] just write today and we can see what it
[00:00:04] does. It generates my to-do list for
[00:00:06] today. It's going to go to Trello and
[00:00:08] see if anybody on my team has added any
[00:00:11] new Trello cards and then it basically
[00:00:13] runs this Python script and then you can
[00:00:15] see it's going to read my Today MD and
[00:00:17] it's going to update it. And you can see
[00:00:18] it popped up here. So, this is a link to
[00:00:20] my research digest, my blog post. It's
[00:00:22] 9,000 words and I wrote it in 1 and 1/2
[00:00:24] days. There is no way I would have done
[00:00:27] this myself. That is insane to me.
[00:00:29] here's how I'm thinking about it. What
[00:00:30] do you think? Oh, I don't really like
[00:00:31] that. What if we try this other way? And
[00:00:33] then I do that throughout the whole
[00:00:34] construction of the blog post. You can
[00:00:36] just be like, "Enter me about my
[00:00:37] business." And then it will ask you a
[00:00:38] bunch of questions and then it will
[00:00:40] write a context file for you. This file
[00:00:42] we're looking at, this profile, I never
[00:00:43] wrote a word of it. Every time I have
[00:00:45] Claude add a context file, I say, "What
[00:00:47] index needs to be [music] updated?" And
[00:00:49] it just figures it out.
[00:00:50] >> Let's say I'm just overwhelmed by all
[00:00:51] this stuff. What are your three tips to
[00:00:52] get started? Whenever you find yourself
[00:00:54] [music]
[00:00:54] explaining context to Claude, stop and
[00:00:57] think about, am I ever going to have to
[00:00:58] explain this context [music] to Claude
[00:01:00] again?
[00:01:01] >> Okay, welcome everyone. Uh my guest
[00:01:03] today is Terresa Torres. Uh Teresa is a
[00:01:05] legend in the PM field. She's author of
[00:01:08] continuous discovery habits, but today
[00:01:10] we're going to talk about how Teresa
[00:01:11] uses cloud code for everything from
[00:01:14] writing to editing to task management to
[00:01:17] coding. uh really excited to get her to
[00:01:19] give us a tour of her cloud code
[00:01:21] projects and to show us how it's
[00:01:22] actually done. So, welcome Teresa.
[00:01:24] >> Thanks for having me. I'm excited to do
[00:01:26] this.
[00:01:27] >> Yeah. Um so, you know, I've also used
[00:01:29] cloud code quite quite a bit, but I I'm
[00:01:31] super interested in seeing your uh
[00:01:32] highle workflow. So, maybe you can give
[00:01:34] us a quick tour first.
[00:01:36] >> Yeah, let me share my screen. Okay, so
[00:01:38] what we're looking at is really simple.
[00:01:40] I have Obsidian here on the left and
[00:01:42] then and if people aren't familiar with
[00:01:43] Obsidian, it's just a note-taking tool
[00:01:45] that's based on Markdown. And then I
[00:01:47] have two terminal windows on the right.
[00:01:49] And the big thing that I use Claude Code
[00:01:52] for like I started using it coding just
[00:01:54] like everybody else most that's most
[00:01:56] people's entry into it. Um but I what I
[00:01:59] really loved about Claude Code with
[00:02:01] coding is it's almost like you're pair
[00:02:03] programming with Claude. And I was like
[00:02:05] wow how do I pair with Claude on
[00:02:07] everything that I do? And so I started
[00:02:10] doing this for writing and for strategy
[00:02:12] and for literally all of the work that I
[00:02:14] do. This is my setup. This is my work
[00:02:17] obsidian vault. So I have an obsidian
[00:02:19] vault called work. In it there's a bunch
[00:02:21] of subdirectories. One of them is LLM
[00:02:24] context which I'll get into that. And
[00:02:26] then my notes which is just any notes
[00:02:28] that I have. I have a research project
[00:02:29] that we can talk through. I have my
[00:02:31] tasks system. Worthy reads are like
[00:02:34] articles that I've saved that other
[00:02:35] people wrote that I really like. And
[00:02:37] then my writing directory. And then you
[00:02:39] can see I have a cloud MD file here. Um,
[00:02:42] and we can kind of go through all of
[00:02:43] this, but I'm going to start with tasks.
[00:02:45] So, the way my task system works is I
[00:02:48] have folders for different things. So, I
[00:02:50] have a folder for bugs. I have a folder
[00:02:52] for ideas. I have a folder for tasks.
[00:02:55] And every day, I launch CL Claude inside
[00:02:58] my tasks folder. So, you can see this
[00:03:00] top terminal window. I'm in tasks. I'm
[00:03:03] just going to launch Claude. And at the
[00:03:05] beginning of my day, I literally just
[00:03:07] write today. And we can see what it
[00:03:09] does. The first thing it's going to do
[00:03:11] is it's going to go to Trello and see if
[00:03:14] anybody on my team has added any new
[00:03:17] Trello cards to my board. You can see,
[00:03:19] good news, there's no new Trello cards.
[00:03:21] I've already run this today, but we'll
[00:03:22] just see what it looks like. And then it
[00:03:24] basically runs this Python script where
[00:03:26] it generates my to-do list for today.
[00:03:28] So, that's what we're looking at here on
[00:03:30] in Obsidian. It says Monday, November
[00:03:32] 10th. I have one overdue item. I have a
[00:03:34] number of items that are due today. And
[00:03:36] then I have my in progress ideas that
[00:03:38] I'm working on. And uh this script just
[00:03:42] generated this file. Every task is a
[00:03:44] markdown file. So you can see in my
[00:03:47] tasks folder, I just have a whole bunch
[00:03:48] of tasks. Basically my this task that's
[00:03:51] overdue was due on Friday. You can see
[00:03:53] it's just I have to call the grooming
[00:03:55] place for my dog and schedule an
[00:03:57] appointment for her and I didn't do that
[00:03:58] yet. Um and then all my other tasks like
[00:04:01] I have calls with a couple people today.
[00:04:04] Um, I'm writing a Claude code safety
[00:04:06] article. I've got to add some images to
[00:04:08] it. All this stuff just shows up on my
[00:04:10] to-do list every day based on what I put
[00:04:12] in my tasks.
[00:04:14] >> Got it. So, the other tasks like the
[00:04:15] calls and stuff, is it coming from your
[00:04:16] calendar or is it coming from just your
[00:04:18] notes?
[00:04:18] >> It's tasks that I've created. And I'll
[00:04:21] show you. We're going to create a new
[00:04:22] task together. I'll show you what that
[00:04:23] looks like.
[00:04:24] >> Got it.
[00:04:25] >> Um, so that's the first thing is when I
[00:04:27] run the today command, I do it every
[00:04:28] morning. It's basically looking through
[00:04:30] my tasks folder and looking for anything
[00:04:33] that's due today or anything that's
[00:04:34] overdue. And then it creates this today
[00:04:37] file for me and it's just telling me
[00:04:39] what do I need to do today.
[00:04:41] >> And then I distinguish between tasks
[00:04:43] that have a due date and ideas that you
[00:04:46] know they're like more like projects
[00:04:48] that don't have a specific due date, but
[00:04:50] they're things that I have going that
[00:04:52] are ongoing. So you can see like I have
[00:04:55] a podcast just now possible that's like
[00:04:57] always in my in progress because it's
[00:04:59] reminding me to like make sure I
[00:05:01] schedule guests and um you can see here
[00:05:04] I have a single episode. This is my
[00:05:07] project for like getting that episode
[00:05:09] ready to be released. Um and then I have
[00:05:11] a task for social media, but this is
[00:05:15] really just my like remember to schedule
[00:05:18] guests kind of thing that's always in
[00:05:20] progress. Um, and so what this does is
[00:05:24] it gives me a lot of flexibility. If I
[00:05:25] just have a random idea, I can just say
[00:05:27] it a cla new idea and it will tell it
[00:05:30] what it is. It will create a markdown
[00:05:31] file. It'll put it in my ideas folder.
[00:05:34] >> Um, if it's a task, I can give it a due
[00:05:37] date and then it will show up on my on
[00:05:39] this like to-do list. This is just
[00:05:42] called my today MD on the day that it's
[00:05:44] due.
[00:05:45] >> Should we try making uh maybe like uh
[00:05:48] record pockets of Peter or something
[00:05:49] like some sort of task?
[00:05:50] >> Yeah. So, we'll do a new task in just a
[00:05:52] second here. The other thing that's
[00:05:53] happening when I run this today command,
[00:05:56] it is I've built this research system.
[00:05:58] So, I'm trying to keep up to date on
[00:06:00] like academic research that's related to
[00:06:03] my um work. And so, I built this system
[00:06:06] that searches a preprint server and then
[00:06:08] Google Scholar every day and it gives me
[00:06:11] a research report of what's relevant to
[00:06:14] my work and that gets added to this
[00:06:17] today list. So you can see right here
[00:06:18] it's not here yet and it's because we
[00:06:20] haven't done that part. So it's running
[00:06:22] this slash command that's part of my
[00:06:24] research project and now it's asking me
[00:06:26] oh it wants to go see if there's a
[00:06:28] research queue. So we're going to say
[00:06:29] yes to that.
[00:06:30] >> And then you'll see it's going to update
[00:06:32] this today list with any research for me
[00:06:34] to review. The Q's empty.
[00:06:38] It's creating my research today MD.
[00:06:42] >> Got it. So this is just like uh
[00:06:44] searching some websites to find new
[00:06:46] research, right? Yeah. Yep. And then you
[00:06:48] can see it's going to read my today MD
[00:06:50] and it's going to update it and you can
[00:06:51] see it popped up here. So this is a link
[00:06:53] to my [snorts] research digest. So that
[00:06:56] that's my today command and you can see
[00:06:57] it gives me a summary like this is what
[00:06:59] I just did. I created your today MD with
[00:07:02] an overdue task 10 in tasks for in
[00:07:05] progress your research whatever. And
[00:07:07] then you can see it's also creating a
[00:07:09] this week view and a next week view.
[00:07:11] >> Got it. Okay. Yeah.
[00:07:12] >> Okay. So let's say I want to do a new
[00:07:13] task. We're actually going to write a
[00:07:14] blog post together. So, I'm going to do
[00:07:17] new task. Um,
[00:07:19] write plan auto except Claude
[00:07:25] blog post. Do today draft
[00:07:31] outline with Claude. And it basically
[00:07:34] this this tasks folder is set up with a
[00:07:36] cloud MD so that Claude knows what to do
[00:07:39] with this. It knows to create a task.
[00:07:41] You can see it's using Obsidian front
[00:07:44] matter and I've defined this whole
[00:07:46] system for Claude so it knows to do
[00:07:47] this. It's defining as a task. It's
[00:07:49] putting the due date as today. It's
[00:07:51] tagging it for me. It's give basically
[00:07:53] giving me kind of a checklist. I It's
[00:07:56] actually not supposed to do this because
[00:07:57] it's kind of a Chromy checklist. Um it's
[00:07:59] supposed to just take my notes, but
[00:08:00] pretty good. We're going to go with
[00:08:02] that. And then let's see if sometimes
[00:08:04] Claude is smart enough to put something
[00:08:05] due today on my today MD. It's not this
[00:08:08] time. So I'm going to say add to today
[00:08:10] MD.
[00:08:11] >> Got it. Okay.
[00:08:12] >> And then what that's going to do is it's
[00:08:13] just going to add that task. You can see
[00:08:14] it's here. So now I have my write plan
[00:08:17] autoac accept mode. What I love about
[00:08:20] this is I work out of the terminal most
[00:08:22] of the day and I keep this tasks
[00:08:24] terminal open all the time. So if like I
[00:08:26] think of something that I have to do or
[00:08:28] I have a random idea, I literally can
[00:08:30] just be like new idea blah blah blah
[00:08:32] blah and it's done. And then I can just
[00:08:34] go back to my work in my other window.
[00:08:37] And it's it's [snorts] a lot faster than
[00:08:39] like opening a web browser, going to
[00:08:41] Trello, creating a new card, setting a
[00:08:43] due date, right? It's just it's super
[00:08:45] fast and that's what I love about it.
[00:08:46] >> Got it. This episode is brought to you
[00:08:48] by Optimize. The problem in marketing
[00:08:51] usually isn't a lack of ideas, it's a
[00:08:53] lack of time. If your to-do list keeps
[00:08:55] getting away from you, then take a
[00:08:56] [music] look at Optimize the Oppo, an AI
[00:08:58] agent platform built visibly for
[00:09:00] marketing. With OPPO, you can use AI
[00:09:02] agents for SEO and geo recommendations,
[00:09:04] AB testing, website analysis, and much
[00:09:06] more. OPPO knows your brand inside and
[00:09:08] out and plugs into your existing tools
[00:09:10] and data systems so that you can save
[00:09:12] [music] time on laborintensive feature
[00:09:14] testing, reporting, and more. See what
[00:09:16] it can take off your plate at
[00:09:17] optimiz.com/ai.
[00:09:20] Now, back to our episode.
[00:09:21] >> The other thing I'll share is it allows
[00:09:23] me to do things like, uh, what are all
[00:09:26] my marketing ideas?
[00:09:29] and it's just going to go search my
[00:09:30] ideas folder for anything related to
[00:09:32] marketing. And so like whenever I'm
[00:09:34] working on a new project, I can just ask
[00:09:36] Claude like what are my tasks related to
[00:09:39] this or what am I what are my idea open
[00:09:41] ideas that are related to this and it
[00:09:43] just goes out and finds them and like
[00:09:45] Trello has search but it's not the best
[00:09:48] frankly.
[00:09:49] >> Okay.
[00:09:50] >> Um so I like this a lot too.
[00:09:52] >> So you have like ideas and memories and
[00:09:53] like random re research snippets that
[00:09:55] you pull.
[00:09:56] >> Yeah. So you can see
[00:09:58] >> like in my tax folder, I have bugs that
[00:10:00] have been filed. I have ideas. Import is
[00:10:03] for if I'm importing a bunch of stuff
[00:10:05] from Trello. I want to review it to make
[00:10:07] sure it imported correctly. My inbox is
[00:10:09] how I get stuff from my phone to my to
[00:10:12] this whole system. Memories is like
[00:10:14] things. It's like little snippets that I
[00:10:16] want to remember. So we can kind of look
[00:10:18] at what's in here. I think this is safe.
[00:10:20] Like I have a affiliate link to the AI
[00:10:22] evals course that I always forget what
[00:10:23] it is. So, it's literally just here's my
[00:10:25] affiliate link. This is a task. I don't
[00:10:27] know actually know why that's in
[00:10:28] memories.
[00:10:30] >> Real real real quick. What do you mean
[00:10:31] by inbox? Like you send an email to
[00:10:33] yourself over the phone or or how does
[00:10:35] it
[00:10:35] >> Yeah. Uh so this this is a little bit of
[00:10:38] a hack and I'm actually moving away from
[00:10:40] it. So I mentioned I moved a bunch of
[00:10:41] stuff and it broke some things. But um I
[00:10:44] was using Dropbox to sync my vaults and
[00:10:48] I'm now moving to Obsidian Sync to sync
[00:10:50] my vaults. So, the Obsidian Sync, I can
[00:10:52] use the iOS Obsidian app and I can just
[00:10:54] access all of this stuff from my phone.
[00:10:56] But when I was using Dropbox, I had to
[00:10:59] set up this is like a iCloud linked
[00:11:02] folder
[00:11:03] >> so that I could add to it from my phone
[00:11:04] and then it would automatically show up
[00:11:06] here and then I could pull it into my
[00:11:08] task system. That was kind of a pain in
[00:11:10] the butt. So, I moved from Dropbox to
[00:11:12] Obsidian Sync to make that easier.
[00:11:13] >> Got it. Okay. So, basically Obsidian and
[00:11:15] Cloud Code run your life right now.
[00:11:17] Yeah, that makes sense. Yeah, pretty
[00:11:18] much cloud code and obsidian read my
[00:11:20] life.
[00:11:20] >> All right, so let's go back to the
[00:11:22] writing the blog post task. So like um
[00:11:24] >> yeah,
[00:11:25] >> how's it going to help us write this
[00:11:26] blog post? Yeah.
[00:11:27] >> So I could do this. Let's do this. We're
[00:11:30] going to get rid of this dumb checklist
[00:11:33] that Claude made because I don't like
[00:11:34] it.
[00:11:36] And we're just going to do like Okay,
[00:11:38] I'm going to talk through I'm just going
[00:11:39] to like talk out loud while I plan out
[00:11:40] my blog post. So for context, I'm in the
[00:11:43] middle of writing this huge cloud code
[00:11:44] series for people that are
[00:11:46] non-technical. And it started with like
[00:11:48] what is cloud code? Why is it different
[00:11:50] from cloud in the browser? And then the
[00:11:52] second post in the series was about like
[00:11:54] how to give claim memory, which if you
[00:11:56] want to get into that, all my context
[00:11:58] files are also here in Obsidian. And
[00:12:00] then the third blog post that's coming
[00:12:02] out this Wednesday is about safety. So
[00:12:04] how to use cloud code safely. And then
[00:12:06] this one we're going to start together
[00:12:07] is the fourth article. And this is where
[00:12:09] I'm going to get into like doing
[00:12:11] projects with Claude. And so I want to
[00:12:14] write a blog post where I talk about
[00:12:15] like plan mode, auto accept mode. And
[00:12:19] then I always want to use examples in my
[00:12:22] blog post that are related to product
[00:12:25] managers. And so like in this blog post
[00:12:28] I might think like let's talk through
[00:12:30] plan mode and auto accept mode if you
[00:12:32] were planning a new feature. So I'm
[00:12:34] starting to think about like what's my
[00:12:36] example going to be in the blog post?
[00:12:38] And I have an AI product called the
[00:12:40] interview coach. This is a product where
[00:12:43] in my class where I teach how to conduct
[00:12:45] effective customer interviews. We do
[00:12:47] practice interviews with each other in
[00:12:48] class and then the students can submit
[00:12:50] their transcripts and get like detailed
[00:12:52] feedback on how good of a job they did.
[00:12:54] And the thing with this product is it
[00:12:56] was built for my storybased interview
[00:12:58] coach or storybased interview class. And
[00:13:01] so the coach gives feedback on
[00:13:03] story-based interviews. And my new
[00:13:06] feature idea is can I extend it to work
[00:13:10] with non-storybased interviews. So this
[00:13:13] is like a feature idea I have. And so in
[00:13:15] the blog post there's a little meta. I'm
[00:13:17] going to use this feature idea to show
[00:13:20] how I would use plan mode and auto
[00:13:23] accept mode. Right. So okay I'm gonna
[00:13:26] this is all I have. This is literally
[00:13:28] the state of this blog post. This is
[00:13:29] real. I have not written a single thing.
[00:13:31] And now I'm going to go over to this
[00:13:33] terminal window on the bottom and I'm
[00:13:34] going to launch Claude. And this is in
[00:13:36] the context of my writing vault. And so
[00:13:39] my writing vault has a claude MD that
[00:13:41] talks about how I like to write and how
[00:13:42] I like to write with Claude. So it has
[00:13:44] different context than this tasks
[00:13:47] window. So like in my writing window, I
[00:13:50] can't type new task. It doesn't know
[00:13:51] anything about my task system. I have to
[00:13:53] do that in my tasks window.
[00:13:55] >> Got it?
[00:13:56] >> So we're going to do this. I don't know
[00:13:58] why it thinks it's a new folder, but
[00:13:59] we're going to ignore that for a minute.
[00:14:01] And then I'm going to say I want help
[00:14:03] creating an outline for a new blog post.
[00:14:06] I do this in plan mode, which is
[00:14:09] actually what the blog post is about.
[00:14:11] You can find my early thoughts
[00:14:15] in Oh, see I would not, this is a little
[00:14:18] weird. I would not do this in the task
[00:14:20] card. What I would do is I would come to
[00:14:22] writing. I would go to my claude code
[00:14:25] series and I would do a new file.
[00:14:28] >> Got it.
[00:14:29] >> Let's do plan mode.
[00:14:33] And that did not go where I wanted it.
[00:14:34] So, we're going to move it in plan mode.
[00:14:37] And I actually did not tell Cloud enough
[00:14:39] information because it's not it's going
[00:14:41] to look for plan mode in the current
[00:14:42] directory, but the plan mode is actually
[00:14:45] in claude code. So, we'll see what it
[00:14:47] comes back with. We'll see if it finds
[00:14:48] it.
[00:14:49] >> Okay. So, basically, you have a CL.
[00:14:51] Okay. So ju just real quick, you have a
[00:14:53] claw.md for your writing vault that has
[00:14:57] a bunch of writing styles and like uh
[00:14:59] you know that kind of stuff, right?
[00:15:00] >> Yep.
[00:15:00] >> Is that got it?
[00:15:02] >> Yeah. So if you look at here on the
[00:15:04] left, like tasks is a pro that you can
[00:15:07] think about tasks is like a claude
[00:15:08] project. I launched this instance of
[00:15:11] claude in the context of tasks
[00:15:13] >> and then I have a writing folder and I
[00:15:15] launched this instance of claude in the
[00:15:17] context of the writing folder. So the
[00:15:20] writing folder has different rules than
[00:15:22] the tasks folder. They each have their
[00:15:24] own cloud MDs. So the cloud MD for tasks
[00:15:27] explains how the task system works. It
[00:15:29] explains how tagging works. It explains
[00:15:30] how front matter in Obsidian works. So
[00:15:32] that when I just type new task, it knows
[00:15:34] exactly what to do with that.
[00:15:36] >> Whereas my writing folder doesn't have
[00:15:38] any of that context. It just knows it.
[00:15:40] Like you can see here, I told it I want
[00:15:42] to write a blog post. It found plan
[00:15:44] mode. It read it. Now it's asking me to
[00:15:46] read my style guide. And that's because
[00:15:48] my cloud MD in my writing folder says
[00:15:50] before we do anything together, start by
[00:15:52] reading my writing style guide.
[00:15:54] >> Got it. Okay.
[00:15:55] >> So, I'm going to go ahead and say yes,
[00:15:56] it can do that.
[00:15:57] >> Do you ever just ask it to like uh skip
[00:15:59] all the permissions because it's kind of
[00:16:00] annoying to
[00:16:00] >> Yeah. You know what I have? So, I just
[00:16:03] moved everything. Everything used to be
[00:16:05] in Dropbox and I had all the permissions
[00:16:08] set up where my tasks could read and
[00:16:10] edit everything inside tasks and writing
[00:16:12] could read and everything inside
[00:16:14] writing. But because I just moved
[00:16:16] everything, those permissions aren't I
[00:16:18] literally moved everything yesterday.
[00:16:20] Uh, and so I haven't copied over those
[00:16:22] permissions yet. I'm learning like when
[00:16:24] you move things in claude, it kind of
[00:16:26] breaks things a little bit. Uh, so it's
[00:16:28] asking me which features do I want to
[00:16:29] focus on? I actually want to do both.
[00:16:32] Um, what's your intended audience for
[00:16:35] this post? Product people new to Claude
[00:16:37] should already know that. That's a
[00:16:38] little disappointing.
[00:16:39] >> Wait, so so like uh is asking you
[00:16:40] questions because you prompted to ask
[00:16:42] your questions? ask me questions because
[00:16:44] it read this plan mode document and it's
[00:16:47] now like trying to get more information
[00:16:49] from me to be helpful. Normally I have a
[00:16:52] little bit more here, right? This isn't
[00:16:54] really enough for Claude to work with
[00:16:56] yet, but let's let's see what Claude
[00:16:58] does.
[00:17:00] >> Yeah, see it's trying to do too much
[00:17:01] right out of the gate, but let's see
[00:17:03] what it does now. I understand the
[00:17:05] direction. Let me create an outline.
[00:17:12] F. It's already got a headline.
[00:17:17] Introduce plan mode and auto accept
[00:17:19] mode. What it is, when to use it, what
[00:17:22] you plan, what it is, the dangers.
[00:17:26] [laughter]
[00:17:27] >> That's great. Yeah,
[00:17:29] >> this is kind of nuts, right? Like it
[00:17:30] kind of went crazy. Um, so I'm going to
[00:17:35] tell it went crazy.
[00:17:36] >> Uh, it's kind of like, uh, when I use
[00:17:37] cloud code to like write a product spec,
[00:17:39] I always wanted to put put the spec in
[00:17:41] MD file so I can delete a bunch of stuff
[00:17:43] because it it tends to do too much, you
[00:17:45] know.
[00:17:46] >> Yeah. So, usually, to be honest, usually
[00:17:48] I have a little bit more. So, let's
[00:17:50] let's actually play with this draft a
[00:17:52] little bit. Um, I would probably give
[00:17:54] Claude something like goals help people
[00:17:58] new to Claude code do bigger projects.
[00:18:04] Claude code uh use
[00:18:07] planning a new feature as a product
[00:18:10] manager as an example throughout. And
[00:18:14] then we could do I can use my personal
[00:18:17] experience with
[00:18:20] expanding the interview coach. I'm going
[00:18:22] to ignore typos for now because Cloud
[00:18:24] won't care.
[00:18:25] >> Um, and then, um, I'm going to do
[00:18:28] something like less about the features,
[00:18:32] these features,
[00:18:35] more about how to get
[00:18:38] Claude
[00:18:40] to do good work. And let's see if this
[00:18:42] helps.
[00:18:46] >> Got it.
[00:18:47] >> Let's see what it comes back with.
[00:18:49] >> So, okay. So after this outline, you're
[00:18:51] going to ask her to do online research
[00:18:53] or what's the I can do next?
[00:18:56] >> Yeah. So you can see already it came
[00:18:58] back and it's like, "Oh, okay. I made
[00:18:59] too many assumptions."
[00:19:01] >> Yeah.
[00:19:01] >> Um and it's like, "Okay, now like now is
[00:19:04] this like the right direction?" So now I
[00:19:06] might now I what I really want to do is
[00:19:08] ask Claude like you asked about
[00:19:10] research. We got to come out of plan
[00:19:12] mode for this. Has anyone else written a
[00:19:15] blog post about this? and I'll go and
[00:19:18] I'll go search and see what other blog
[00:19:19] posts are out there. So, I'll often do
[00:19:22] this. I'll often like before I sit down
[00:19:23] to write, I want to know what else has
[00:19:25] been out there. If somebody else has
[00:19:27] written this article for my audience,
[00:19:29] I'm not going to write it. I'm just
[00:19:31] going to like write a different article
[00:19:32] and just link to that article. Um, I
[00:19:34] want to make sure that I'm writing stuff
[00:19:36] that's unique.
[00:19:37] >> And then now sometimes someone may have
[00:19:39] written this blog post like in the
[00:19:40] context of coding and that's fine. Most
[00:19:42] of my audience isn't going to read that.
[00:19:44] And so, but I can read that article and
[00:19:46] learn from their experience and then
[00:19:48] translate it to product management. Um,
[00:19:50] so I always use Claude Code to like do
[00:19:53] searches for me. The other thing I use
[00:19:55] it for while I'm writing is like I'll
[00:19:57] make a claim and I'll be like, "Is that
[00:19:59] claim true?" And then I'll ask Claude
[00:20:01] like, "Can you do some academic research
[00:20:02] for me and see if there's evidence
[00:20:04] behind this? Like, is this really a true
[00:20:06] claim or is it just something that I
[00:20:07] randomly believe?" So, let's see what
[00:20:09] Claude came back with. So, a lot of
[00:20:11] people have written about this. Of
[00:20:12] course, Anthropic has written about it.
[00:20:14] They have great documentation. Most are
[00:20:16] written for developers, engineers. Yeah.
[00:20:18] Perfect.
[00:20:19] >> I think people wrote like technical
[00:20:20] stuff about plano but not about this use
[00:20:22] case.
[00:20:22] >> Yeah. So then I might ask like okay um
[00:20:26] how do people search for this kind of
[00:20:29] content?
[00:20:31] What keywords from an SEO standpoint
[00:20:35] should I keep in mind? I almost never do
[00:20:37] this to start. I do this at the end, but
[00:20:39] we can do it to see how it does. Oh,
[00:20:41] that's very smart. I I I never asked
[00:20:43] this question for my blog post, so
[00:20:45] that's that's that's important. Yeah.
[00:20:47] >> And again, it just goes off and does its
[00:20:49] thing, and I let it do its thing, and
[00:20:50] the meanwhile, I'll be like over here
[00:20:51] noodling. I'm like,
[00:20:53] >> how am I going to how am I going to
[00:20:54] structure this blog post? And like this
[00:20:57] is really stubbed out. There's not
[00:20:58] really a blog post here, right? So
[00:21:01] >> I might start to think about an outline
[00:21:02] and be like okay well the introduction
[00:21:06] needs to be strong hook around value of
[00:21:11] doing project work with claude code.
[00:21:15] Um then introduce
[00:21:18] like claude modes
[00:21:20] plan auto accept
[00:21:23] um reference
[00:21:25] safety article
[00:21:27] um walkth through detailed example
[00:21:32] interview coach. So let's see what it
[00:21:34] came back with. So I found it's really
[00:21:37] good at keyword research
[00:21:39] >> like really good at keyword research. I
[00:21:42] tend to do this after I've written the
[00:21:43] article because I really want to write
[00:21:44] my articles for humans, but then I might
[00:21:47] tweak some words in my subheaders or my
[00:21:49] titles to to like target higher volume
[00:21:52] keywords.
[00:21:53] >> What what what is it actually doing? Is
[00:21:54] it just using Google searches here or is
[00:21:56] it actually doing some uh fancy stuff to
[00:21:58] >> Yeah, you can see it's just doing
[00:22:00] searches and looking for what's ranking
[00:22:01] well.
[00:22:02] >> Oh, is that what it's doing?
[00:22:03] >> Yeah.
[00:22:03] >> Oh, interesting. Okay.
[00:22:04] >> Yeah.
[00:22:05] >> Okay.
[00:22:05] >> So, it's sort of my SEO researcher.
[00:22:07] >> Interesting. And then I could be like,
[00:22:09] I've started to stub out an outline in
[00:22:14] plan.
[00:22:16] Can you suggest
[00:22:18] alternative structures? There's not
[00:22:21] enough meat here. It's probably not
[00:22:22] going to do a very good job here, but
[00:22:24] >> um we'll see what it does. And so I do
[00:22:27] this. This is literally how I write. I'm
[00:22:29] like doing all my thinking really rough.
[00:22:31] I'm going back and forth with Claude.
[00:22:34] I'll have questions like what do I do?
[00:22:36] like how does this work in Claude? Like
[00:22:38] I think I know how auto accept mode
[00:22:40] works, right? But then I'll be writing a
[00:22:41] blog post about it. I'll be like, is
[00:22:42] that really right? And I literally will
[00:22:45] just pop over here and be like, Claude,
[00:22:46] is that are you allowed to do this in
[00:22:47] auto accept mode? Um, and so that's
[00:22:50] really nice, too. And I know this is a
[00:22:52] little meta. I'm writing a blog post
[00:22:53] about Claude code, but Claude can
[00:22:55] actually answer questions about
[00:22:56] anything, right? So, I could be writing
[00:22:58] a blog post about how product teams do
[00:23:01] customer interview analysis and I can
[00:23:03] still ask Claude, in fact, I wrote a
[00:23:04] blog post about how about customer
[00:23:06] interview analysis with AI. And when I
[00:23:09] was writing that article, I was
[00:23:10] constantly asking Claude to look at
[00:23:12] research for me, like academic research,
[00:23:14] like what do we know about what is lost
[00:23:17] when we rely on AI synthesis? What do we
[00:23:19] know? And a lot of that came from just
[00:23:21] asking Claude to do the research for me.
[00:23:23] >> Got it. So it's very much two screen uh
[00:23:26] kind of process. Yeah, they're
[00:23:28] definitely using as a thought partner
[00:23:29] and like a researcher along the way.
[00:23:31] >> And so you can see here now Claude came
[00:23:33] back with like here's some other ways to
[00:23:34] structure it. So we could do example
[00:23:36] first structure,
[00:23:38] uh problem solution structure,
[00:23:42] journey structure, like your personal
[00:23:43] story. And you can see for each it's
[00:23:45] it's kind of like giving me a rough
[00:23:48] outline. So, what I like about this is
[00:23:50] like when I write, I usually have a
[00:23:52] pretty fixed idea of what the structure
[00:23:54] is in my head. And Claude helps me
[00:23:57] explore alternatives. So, it's like I'm
[00:23:59] comparing and contrasting in the context
[00:24:01] of writing, which before working with
[00:24:03] Claude, I would have literally never
[00:24:05] done that. And then the other thing that
[00:24:07] it really helps me with, and maybe I'll
[00:24:09] pull up my web browser to show this. Um,
[00:24:11] let me think about actually I think I
[00:24:13] can show it right here. Um the article
[00:24:16] that I'm publishing this coming
[00:24:17] Wednesday is on safety. So it's how do I
[00:24:20] teach beginners cloud code beginners how
[00:24:22] to run an LLM safely on their computer.
[00:24:26] And you can see I'll show you every it's
[00:24:29] organized by tier. So like what's the
[00:24:30] risk of letting it read files and then
[00:24:33] at the end of every section I include
[00:24:35] what cla is doing and how you know what
[00:24:38] it's doing. So like there's these tables
[00:24:39] of like this just indicates if it's
[00:24:41] reading. There's like cuz like I'm
[00:24:43] assuming most of my readers don't know
[00:24:44] Unix commands, right? So
[00:24:46] >> yeah, probably not using terminal. Yeah.
[00:24:48] >> And there's no way I would have written
[00:24:50] this article. I'll show you at the
[00:24:52] bottom. Look at all these. Look at what
[00:24:53] we cover. Like it's insane. This blog
[00:24:56] post is enor. You can see it's like
[00:24:57] 8,800 words. And I created this like
[00:25:00] quick reference commands table. This is
[00:25:02] like how Claude reads. This is how it
[00:25:04] searches beyond your current directory.
[00:25:06] This is how it searches the web. This is
[00:25:08] how it writes files. This is how it
[00:25:09] executes code. And like this is an
[00:25:13] awesome reference now for people that
[00:25:14] have never used Claude code. There is no
[00:25:17] way I would have done this myself.
[00:25:19] Claudia.
[00:25:20] >> So you're Yeah.
[00:25:21] >> I started to generate a list like you
[00:25:24] can see in my outline like I started to
[00:25:27] generate a list of like commands as I
[00:25:31] used Claude like oh this stuff should go
[00:25:33] in my document but as I worked with
[00:25:35] Claude it taught me like oh I also used
[00:25:38] these other commands and it so this blog
[00:25:41] post is way more thorough than it would
[00:25:43] have been if I had just done it on my
[00:25:45] own. co-authoring with Claude along
[00:25:47] along the way like section by section.
[00:25:49] Yeah.
[00:25:49] >> Yeah. And then the other thing that I do
[00:25:51] is like once I get to a complete
[00:25:53] outline, I actually start writing and I
[00:25:55] still do all of my own writing. I want
[00:25:57] it to be in my voice. I personally like
[00:25:59] to write and I have I feel like I have a
[00:26:01] very specific cadence to my writing that
[00:26:03] like Claude just doesn't really get. It
[00:26:05] gets close but not really. And so what
[00:26:07] I'll do is once I have a really detailed
[00:26:09] outline, I will write a section. And
[00:26:12] then as soon as I'm done with the
[00:26:13] section, I just pop over here and I'll
[00:26:15] say like, "Claude, I wrote the intro.
[00:26:17] Give me feedback."
[00:26:19] >> And then Claude can see the same file I
[00:26:21] can see, right? So I don't have to cut
[00:26:23] and paste anything. And then Claude will
[00:26:25] give me feedback and then it always
[00:26:26] finds typos and it'll just be like, "Do
[00:26:27] you want me to fix the typos?" And I can
[00:26:29] just type yes.
[00:26:30] >> Why don't we try it? Can you get it to
[00:26:31] fix the typos right here? Like does it
[00:26:33] edit your file?
[00:26:34] >> Yeah.
[00:26:34] >> Yeah. Can you fix the typos in my plan
[00:26:39] mode?
[00:26:41] Got it. Yeah.
[00:26:42] >> And it's just going to go and do it. Um,
[00:26:44] so you can see here it's showing me a
[00:26:46] diff of what it's fixing. Um, I don't
[00:26:48] want it just fixing random typos in my
[00:26:50] blog post as I write. So, one thing I've
[00:26:53] taught Claude to do is when we review a
[00:26:55] section, first it tells me what's
[00:26:57] working well. Then it tells me what
[00:26:58] could be better or what could be clear,
[00:27:00] it does a technical review. Am I saying
[00:27:02] anything that's technically wrong? And
[00:27:04] then the last thing it does is it lists
[00:27:06] the typos that it found. and it asks me
[00:27:08] if I want to fix those typos. And that's
[00:27:10] just sort of a safety check. Sometimes
[00:27:12] like I'm using a word that it thinks is
[00:27:13] a typo, but it's not. And so it allows
[00:27:15] me to quickly look down like this is
[00:27:17] kind of an example. This is one it told
[00:27:18] me after the fact. But when we're doing
[00:27:20] our section by section review, it'll be
[00:27:22] like here's what I want to change. And
[00:27:24] then I can just say yes, change it all.
[00:27:26] Or I can be like yes, change it all, but
[00:27:28] don't change this one.
[00:27:29] >> Got it. Got it. Got it.
[00:27:29] >> So I kind of still keep like safety
[00:27:32] guardrails on claude before it just
[00:27:34] starts editing my blog post.
[00:27:35] >> Interesting. It's interesting that you
[00:27:36] still Okay, so you still manually write
[00:27:38] the actual blog post from a detailed
[00:27:40] outline. You still write it your
[00:27:42] >> Yeah, I've experimented with letting
[00:27:44] Claude write stuff.
[00:27:46] >> Um I don't like the voice and Claude
[00:27:49] knows a lot about my writing. Like I
[00:27:50] have my entire product talk archives in
[00:27:53] here. I have taken the time to develop a
[00:27:56] really good writing style guide. For me,
[00:27:57] good writing has a cadence that like you
[00:28:00] can hear. And that's the part of my
[00:28:03] writing like I just can't get Claude to
[00:28:05] get 100% right. And then I also like to
[00:28:08] write to figure out what I think. And so
[00:28:10] like I don't want to outsource all of
[00:28:11] that to Claude because I want to force
[00:28:13] myself to do the thinking myself.
[00:28:15] >> Got it. Got it.
[00:28:16] >> I'm using Claude almost like a sparring
[00:28:18] partner. So like here's how I'm thinking
[00:28:20] about it. What do you think? Oh, I don't
[00:28:22] really like that. What if we try this
[00:28:23] other way? Um and then I do that
[00:28:25] throughout the whole construction of the
[00:28:27] blog post.
[00:28:27] >> Yeah. It's like having a editor and a
[00:28:30] researcher and like you know just kind
[00:28:32] they're sitting there with you, right?
[00:28:33] >> But like full-time, right? It's not like
[00:28:35] I did everything and then you edit it.
[00:28:37] We're doing it very collaboratively.
[00:28:39] >> And then the other piece that I really
[00:28:40] like is that the way that I used to
[00:28:42] write, I used to write like a 2 to
[00:28:43] 3,000word blog post in like three or
[00:28:46] four days. And a reason why it would
[00:28:48] take so long is I would write a section
[00:28:50] and writing is exhausting, right? And so
[00:28:53] at the end of writing a section, I'd be
[00:28:54] like, I'm going to go check my email.
[00:28:55] and then I'd go get distracted for an
[00:28:57] hour and then I come back and write
[00:28:58] another section. But when I'm writing
[00:29:00] with Claude, as soon as we finish the
[00:29:02] review of a section, Claude's always
[00:29:04] like, "Are you ready for phase two?" And
[00:29:06] I'm like, "Yeah, [clears throat] okay. I
[00:29:07] guess I am ready for phase two." So just
[00:29:10] having Claude like poke me, I maintain
[00:29:12] momentum. And so I now a lot of my blog
[00:29:15] posts are a lot more in-depth. They're a
[00:29:17] lot more detailed. They're getting
[00:29:18] longer. Um like you can see this blog
[00:29:21] post is pretty darn long. But you'll see
[00:29:24] there's there is literally no fluff.
[00:29:26] Like I challenge people. This article is
[00:29:28] coming out on November 12th. Um, go read
[00:29:31] it. You can tell me if you think there's
[00:29:33] any fluff in it. Like to me, this is
[00:29:36] just a very detailed guide for how to
[00:29:39] work with Claude safely. And I wrote all
[00:29:42] of this myself. It's 9,000 words and I
[00:29:45] wrote it in one and a half days.
[00:29:46] >> Wow.
[00:29:47] >> Like that is insane to me.
[00:29:49] >> Okay, let let me ask you like a few
[00:29:50] questions about this process. Yeah.
[00:29:52] >> So, so you have one window open for
[00:29:54] writing, do you just uh do you ever
[00:29:56] clear the context or you just keep keep
[00:29:57] going and and you let
[00:29:59] >> That's a really good That's a really
[00:30:01] good question. When I'm working on an
[00:30:03] outline, like when we're developing, so
[00:30:05] like in this writing exercise, we're
[00:30:07] developing an outline, I try to keep all
[00:30:10] of it in the context of the same
[00:30:11] conversation.
[00:30:12] >> Okay?
[00:30:12] >> There will be times like I'll keep an
[00:30:14] eye on whether or not it's going to want
[00:30:15] to compact the conversation. I always
[00:30:17] try to keep Claude from compacting. Like
[00:30:20] if it looks like that's getting close,
[00:30:21] what I'll do is I'll be like, "Claude,
[00:30:23] we're going to run out of context
[00:30:24] window. Let's write a summary of where
[00:30:27] we are that you can read in when I clear
[00:30:30] the context window." And the reason why
[00:30:32] I do that is I want oversight on how
[00:30:34] Claude is compacting the conversation.
[00:30:36] Whereas, if you use the compact, like if
[00:30:38] you just let Claude use its own compact
[00:30:39] tool when you run out, I find that it
[00:30:41] loses a lot of context and detail that I
[00:30:44] don't want it to lose. So, one thing
[00:30:46] that I've done, I don't always do this
[00:30:47] with writing, but I always like when I'm
[00:30:49] working on a project with Claude, in
[00:30:51] fact, that needs to go in this blog
[00:30:53] post. So, I'm glad we're talking through
[00:30:55] this. Uh, I have Claude create this
[00:30:58] document called process notes. And as
[00:31:01] we're working, if it looks like we're
[00:31:03] getting towards the end of the compact,
[00:31:04] the context window, I'll stop and have
[00:31:07] Claude update process notes. And process
[00:31:10] notes is just a text file that's like,
[00:31:12] here's what we did in every session. so
[00:31:15] that I have a history of what we've done
[00:31:16] in the decisions that we've made. And
[00:31:18] then sometimes Claude like just loses
[00:31:21] stuff in the context window. I can be
[00:31:23] always be like, can you just search
[00:31:24] process notes? Like I feel like we
[00:31:26] already made this decision. Um and so
[00:31:28] this is a habit I've gotten into
[00:31:30] whenever I work with Claude and anything
[00:31:31] meaty.
[00:31:32] >> We're constantly co-creating process
[00:31:34] notes together. And I'm getting to the
[00:31:36] point where like I have a a process for
[00:31:39] my process notes where I'm gonna write a
[00:31:42] sub agent that's my document that Claude
[00:31:45] will just call to write those process
[00:31:46] notes when we're running out of context
[00:31:48] window.
[00:31:49] >> Okay, got it. [laughter]
[00:31:50] You've gone to like uh this is like
[00:31:52] inception. You have like
[00:31:53] >> Yeah.
[00:31:54] >> processes for I mean this is the hard
[00:31:56] part, right? Like when the context
[00:31:58] window fills up, bad things happen. Like
[00:32:00] I think you waste a lot of work. Claude
[00:32:03] loses details.
[00:32:04] >> Yeah. He gets dumber. it just gets
[00:32:05] dumber. And so I feel like it's our job,
[00:32:08] at least for now, to like
[00:32:10] >> maintain this process so that when
[00:32:13] Claude resets and its memory gets wiped,
[00:32:16] it can pick up where you left off and
[00:32:17] you'll be fine. Anthropic has tried to
[00:32:19] build that in with that compact
[00:32:21] conversation feature, but it's it's not
[00:32:24] very good. So I like to I like to manage
[00:32:26] it myself a little bit more.
[00:32:28] >> Well, I think that's the thing with this
[00:32:30] uh this like that that's the thing with
[00:32:32] clock code. It just like it's it's
[00:32:35] really kind of made for power users to
[00:32:36] be honest like who really want to
[00:32:37] personalize every everything like it's
[00:32:39] not super it's not super intuitive to
[00:32:41] use if you're a complete beginner but
[00:32:42] you have to like go into the rabbit hole
[00:32:45] >> and it gets more and more powerful.
[00:32:47] >> You know what I like about it though for
[00:32:48] product people is that like using cloud
[00:32:52] code right now and especially pushing
[00:32:53] the boundaries with cloud code is living
[00:32:55] on the edge of what's possible today.
[00:32:57] And I feel like if we're going to build
[00:32:59] with AI, like as product people, if
[00:33:01] we're going to build AI into our
[00:33:02] products, like we should be living on
[00:33:04] that edge. And so like even just the
[00:33:06] stuff we talked about with context
[00:33:08] windows, I wouldn't have learned any of
[00:33:10] that if I hadn't been in cloud code all
[00:33:12] day every day. And so now when I go work
[00:33:14] on like my AI product, when I'm working
[00:33:16] on my interview coach, I have like a
[00:33:18] depth of experience of understanding how
[00:33:20] to manage a context window that there's
[00:33:22] no way I would have developed otherwise.
[00:33:24] And so like yeah, like in the long run,
[00:33:26] is this how we're going to work with
[00:33:27] LLMs? Probably not. Like there'll be
[00:33:29] tooling around it and the labs will get
[00:33:31] better at managing the context for us.
[00:33:34] But like as product people, we can't
[00:33:35] wait for that. We're building AI into
[00:33:37] our products today. So I feel like we
[00:33:39] have to be living on that edge so we can
[00:33:41] build our products on the edge as well.
[00:33:43] >> Yeah. You got to build on the edge. You
[00:33:44] got to learn the latest info.
[00:33:46] >> Yeah.
[00:33:46] >> So that's kind of uh I I just want to
[00:33:48] kind of talk about the context window
[00:33:49] thing a little bit more. So you know so
[00:33:52] so context is like everything for how
[00:33:54] effective these LMS work right. So I
[00:33:56] just want to talk about the three the
[00:33:58] three layers of context that you talked
[00:34:00] about in your previous blog post.
[00:34:01] >> Yeah.
[00:34:02] >> And uh you don't have to maybe share
[00:34:04] your cloud MD file but maybe like talk
[00:34:05] about maybe start with the highest layer
[00:34:07] and talk about what you put in there and
[00:34:08] then and then kind of like you know
[00:34:10] >> Yeah. So I actually have that article
[00:34:12] right here. Let's see. Let's see what
[00:34:15] state it's in. So this article is life.
[00:34:17] You can find it at producttalk.org. And
[00:34:19] in this article, I just talk about like
[00:34:21] the opening hook is this story about how
[00:34:23] I just got sick of trying to get Claude
[00:34:26] and chat GPT to like be reliably good.
[00:34:29] And I realized that like one of the
[00:34:30] challenges is that in order for Claude
[00:34:33] to be good, it needs to know all about
[00:34:35] me and my business. It needs to know
[00:34:36] that I'm a product discovery coach. It
[00:34:38] needs to know that I write at Product
[00:34:40] Talk. It needs to know that my audience
[00:34:41] is crossunctional product teams. It
[00:34:43] needs to know that I have a course
[00:34:45] business and what all those products
[00:34:46] are. It even needs to know things like
[00:34:48] who I work with, right? In order for me
[00:34:51] to say like not only in my task window,
[00:34:54] I can't I can add tasks to my to-do
[00:34:56] list, but I can also say create a Trello
[00:34:59] card on Wena's board and Wena is my
[00:35:02] admin, right? And so I can be like
[00:35:04] create a TR or I can even better I can
[00:35:07] create a task file in my system in
[00:35:09] Markdown and then say create a Trello
[00:35:11] card on Wenna's board using this task.
[00:35:14] So it's like in my system I'm creating a
[00:35:16] task for Willena and then Claude goes
[00:35:18] and pushes it to her Trello board. But
[00:35:20] okay, that only works if Claude has the
[00:35:22] context like who's Wena and what's her
[00:35:24] Trello board and like what's a task,
[00:35:27] right?
[00:35:27] >> Yeah.
[00:35:28] >> So in order to get this like I wrote
[00:35:30] some pretty lazy stuff new task blah
[00:35:32] blah blah blah like in order for that to
[00:35:34] work Claude has to have this view that
[00:35:37] we're looking at doesn't have images but
[00:35:39] I just explained this idea that every
[00:35:40] conversation starts from scratch. We
[00:35:42] have to create memory. Memory has three
[00:35:45] layers. You asked about the three
[00:35:46] layers. The first one is my global
[00:35:48] preferences.
[00:35:50] >> Let me actually pop over to the web
[00:35:51] because I can show some of my CloudMD
[00:35:54] files pretty safely.
[00:35:55] >> Okay.
[00:35:56] >> So, this is my global cloud MD. The
[00:35:58] start of it. Um, I can zoom in a little
[00:36:01] bit.
[00:36:01] >> Perfect. Yeah.
[00:36:03] >> Um, this top section I write about in
[00:36:05] the blog post is just a little thing I
[00:36:07] learned is that like I don't write my
[00:36:10] Claude MDs anymore. Whenever I'm working
[00:36:12] with Claude, when we're done working, I
[00:36:14] say, "Hey, Claude, what did you learn
[00:36:15] about working with me? Like, what should
[00:36:17] we add to the Claude MD so this goes
[00:36:19] smoother next time."
[00:36:21] >> And that's been awesome because I don't
[00:36:23] have to maintain this file anymore.
[00:36:24] Claude does. But you can see like I've
[00:36:26] just defined some personal preferences.
[00:36:28] Like I always want to plan before Claude
[00:36:30] does anything. I never let Cla Claude
[00:36:32] just do stuff. Um, and I do plan at
[00:36:35] multiple levels. You could saw that with
[00:36:36] the blog post. Like I start with just
[00:36:38] really rough thoughts. We work our way
[00:36:40] to an outline. Once I have an outline,
[00:36:42] we start writing. So there's just this
[00:36:45] this file is across all my projects,
[00:36:47] coding, writing, tasks, everything. I
[00:36:50] just want Claude to know like this is
[00:36:52] what I like. And it's not very long.
[00:36:54] This file doesn't go much further behind
[00:36:56] be beyond this. It's pretty short. I
[00:36:58] just have a little section on what how I
[00:37:00] prefer to get feedback from Claude. And
[00:37:02] it's really simple. And this lives, you
[00:37:04] can see here, it lives in my local user
[00:37:08] directory. So on my Mac it's like tilda
[00:37:11] ttorus and thencloud cloudmd.
[00:37:14] >> Yeah. Do you put like theres as a
[00:37:15] product coach and like you know here's
[00:37:17] my business and all that.
[00:37:18] >> All I don't put any of that here because
[00:37:21] this file is going to get loaded in the
[00:37:23] context window every single time you use
[00:37:25] claud.
[00:37:26] >> Got it.
[00:37:27] >> So you only want to put stuff in here
[00:37:29] >> that you always want it to follow. And
[00:37:32] so like if I'm using cloud to like
[00:37:33] brainstorm Christmas gifts for my
[00:37:35] husband, Claude does not need to know
[00:37:36] about product talk.
[00:37:37] [laughter and snorts] So I don't want
[00:37:39] that here, right? But no matter what,
[00:37:42] >> you want to keep this short. Yeah.
[00:37:43] >> Yeah. This is literally global. So you
[00:37:45] want to keep it short. It's going to go
[00:37:46] in every single context window. And like
[00:37:49] I ask Claude all the time, can my dog
[00:37:50] eat this food? Like Claude doesn't need
[00:37:52] to know about product talk for those
[00:37:53] stupid queries.
[00:37:54] >> Right. Okay. Got it.
[00:37:56] >> Like what's really important is you have
[00:37:58] to keep the context window as clean as
[00:38:01] possible.
[00:38:02] >> Yeah.
[00:38:02] >> Right. And so this literally is just my
[00:38:05] global rules. But you'll see later if we
[00:38:08] just scroll down, I have project
[00:38:09] specific instructions. So this is
[00:38:11] actually my writing cla MD. And in my
[00:38:14] writing cla MD, I have like it says at
[00:38:17] the start of each section, read my
[00:38:18] writing style guide. This is actually
[00:38:21] old. I moved things out of Dropbox. But
[00:38:23] if you remember, if I go back to the
[00:38:25] terminal, which is hard to do with this
[00:38:28] sharing thing here, um when I ran um
[00:38:32] sorry, here when I said, "Let's work on
[00:38:33] a blog post together," the very first
[00:38:35] thing Claw did was it went and read my
[00:38:37] writing style guide.
[00:38:39] >> That's right. Yeah.
[00:38:40] >> And it's somewhere in here. Yeah. And
[00:38:42] that's because here it says at the start
[00:38:44] of every session, read the writing style
[00:38:46] guide.
[00:38:47] >> Okay.
[00:38:48] >> And then this is where I get into my
[00:38:50] rules about writing. So Claude is a
[00:38:52] thought partner, not a writer. You're
[00:38:54] acting as an editor. You can do some
[00:38:56] research and development. And this
[00:38:58] document is also not very long. It's
[00:39:01] really just telling Claude, "This is how
[00:39:02] we write together."
[00:39:04] >> Okay.
[00:39:04] >> One thing that is in my global claude
[00:39:07] MD, which I don't, let's see if I have a
[00:39:10] screenshot of it somewhere, is [snorts]
[00:39:11] this idea of context. So I have my I
[00:39:15] have my context files defined. So I've
[00:39:18] created little markdown files. And the
[00:39:20] key is they're little. So I have a lot
[00:39:23] of them because I want to I want to mix
[00:39:27] and match them so that I can tell Claude
[00:39:30] which files matter for the task at hand
[00:39:32] and it doesn't have to read all of my
[00:39:34] context every time. So I have a business
[00:39:37] profile that just is like this is what
[00:39:39] my business does. Here's where you can
[00:39:41] find my product descriptions. Here's
[00:39:43] where you can find my marketing
[00:39:44] channels. Here's where you can learn
[00:39:45] about my team. I can show you that one.
[00:39:47] But it basically is telling Claude where
[00:39:49] to find more details in all these files.
[00:39:52] And so I think this blog post has a
[00:39:54] screenshot of that. Yeah. So this is my
[00:39:56] global cloudmd. We already looked at
[00:39:58] this top part. You can see at the bottom
[00:40:01] I'm telling it here's where you can find
[00:40:03] reference context files. And I basically
[00:40:05] tell it specifically
[00:40:08] only use these files if they're relevant
[00:40:10] to what I'm asking you about.
[00:40:12] >> So if I'm asking you about something
[00:40:13] related to my business, go look at my
[00:40:15] business profile. And if I'm asking you
[00:40:17] something personal, go look at my
[00:40:18] personal profile. And then you
[00:40:20] >> Okay, this makes sense. So you don't
[00:40:21] have to like load a lot of into the
[00:40:23] default context. Yeah. So you don't
[00:40:24] crowd the context.
[00:40:25] >> Exactly. So like if I ask it, I have a
[00:40:28] product file all about my storybased
[00:40:29] customer interview course. So if I ask
[00:40:31] it like, hey, let's work on the landing
[00:40:34] page for my storybased customer
[00:40:35] interview course. It already knows where
[00:40:37] to find details about this course. It
[00:40:39] already knows details about my company.
[00:40:41] It already knows details about my target
[00:40:42] audience. I don't have to tell it any of
[00:40:44] that stuff. And it's because I've given
[00:40:46] it an index of context files so it can
[00:40:49] just go pull in the relevant stuff.
[00:40:51] >> Wow. Okay. But don't you feel like uh
[00:40:53] there's going to be like too many files
[00:40:55] to manage or like I guess you you just
[00:40:56] make cla update your context files,
[00:40:58] right? Is that [laughter]
[00:41:00] >> So I do in this article I talk about
[00:41:03] this. By the way, this article has a
[00:41:05] really fun use case of like how to use
[00:41:07] cloud to do a competitive analysis. So
[00:41:09] you can see here I'm having Claude like
[00:41:11] >> this isn't for me. I used 11 Labs as my
[00:41:13] as if that was my company. Um, and it's
[00:41:16] generating like uh let's see if I can
[00:41:19] find it. I don't know if I'm going to
[00:41:21] find it. But here's the goal. Like the
[00:41:23] key is to give Claude just enough to go
[00:41:25] find what it needs when it needs it. And
[00:41:28] part of this article is about like,
[00:41:31] okay, well, how do I maintain all this
[00:41:32] stuff? Like I have a ton of files now.
[00:41:34] How do I keep it current? And so what I
[00:41:37] do is I have this section about like,
[00:41:40] okay, how do I keep it up to date? The
[00:41:41] way we're going to keep it up to date is
[00:41:43] at the end of every session with Claude,
[00:41:45] I literally say, "What did you learn
[00:41:47] about me that we should add to a context
[00:41:49] file?" And then we have a conversation
[00:41:51] about where to add it. Should it go in a
[00:41:53] cloud MD? Should it go in one of these
[00:41:55] LM context files? Um, like what's the
[00:41:58] right place? And then I'm working with
[00:42:00] Claude to make sure like Claude wants to
[00:42:02] jam everything into your CloudMD. You
[00:42:04] don't want that. That's getting loaded
[00:42:06] in every conversation. So I work with
[00:42:08] Claude to be like, "Hey, it seems like
[00:42:10] that should go in my marketing channels
[00:42:11] file. Why don't we add that there?"
[00:42:13] >> Got it.
[00:42:14] >> So I think about it as like information
[00:42:16] about me and my business goes in a
[00:42:18] context file. Whereas my working
[00:42:20] preferences like this is how me and
[00:42:22] Claude work together goes in a cloud MD.
[00:42:24] >> So basically, yeah, this is a really
[00:42:26] important tip. Like after every
[00:42:28] conversation, you ask Claude, how can
[00:42:29] you make the context better? And you
[00:42:31] have all your contexts in the LM context
[00:42:33] folder with a bunch of sub subfolders
[00:42:36] and files.
[00:42:37] >> Yeah.
[00:42:37] >> Right. Yeah. Wait, so how much are you
[00:42:39] playing this uh cloud employees? They
[00:42:42] sound pretty useful. How much are you
[00:42:43] paying? [laughter] 200 bucks a month.
[00:42:45] >> Uh yeah, I'm on the $100 a month plan.
[00:42:49] >> Okay.
[00:42:49] >> So you can see I'll show you here in in
[00:42:52] Obsidian. You can see all my context
[00:42:54] files. So like for my business, I have a
[00:42:58] target audience file, a marketing
[00:43:00] profile, a list of my differentiators,
[00:43:02] my company overview, my business model.
[00:43:04] >> I didn't like sit down and create this
[00:43:06] all one day. That would have been
[00:43:08] tedious and horrible.
[00:43:09] >> I basically anytime I felt like I needed
[00:43:12] to describe something to Claude, instead
[00:43:15] of just doing it that one time and then
[00:43:17] having to repeat it later, I'd be like,
[00:43:19] "Oh, Claude, in order to do this task, I
[00:43:21] feel like you need to know about my
[00:43:22] differentiators. Maybe interview me."
[00:43:24] And I literally claude will interview
[00:43:26] you can just be like interview me about
[00:43:28] my business and then it will ask you a
[00:43:30] bunch of questions and then it will
[00:43:31] write a context file for you based on
[00:43:33] what you learned.
[00:43:34] >> Got it. Okay.
[00:43:35] >> Um so that's that's a lot of how I did
[00:43:37] most of this stuff.
[00:43:38] >> Okay. Yeah. As long as you just sat down
[00:43:40] one day and made all these folders,
[00:43:41] right? It's not
[00:43:42] >> No, I add to it like gradually over
[00:43:44] time.
[00:43:44] >> So what about like uh Okay, last
[00:43:46] question. Let's say I'm just overwhelmed
[00:43:48] by all this stuff. like this is like
[00:43:51] [laughter]
[00:43:51] >> like I want to learn stuff but like it
[00:43:53] sounds like you really personalize it
[00:43:55] for your life.
[00:43:56] >> Yeah.
[00:43:56] >> Like what are your three tips to get
[00:43:57] started? Let's say I already use cloud
[00:43:59] code for like co coding but I want to
[00:44:01] use it to manage my life.
[00:44:02] >> The first thing is with context you
[00:44:05] don't have to get here overnight. Like
[00:44:08] >> I think the simplest rule is whenever
[00:44:10] you find yourself explaining context to
[00:44:12] Claude, stop and think about am I ever
[00:44:15] going to have to explain this context to
[00:44:17] Claude again? And honestly, the answer
[00:44:18] is probably yes. So instead of
[00:44:21] explaining it to Claude, change tasks
[00:44:23] just for a minute and just be like,
[00:44:24] "Claude, I need to explain some context
[00:44:25] to you. Let's capture it in a context
[00:44:27] file."
[00:44:28] >> Got it. Yep, that makes sense.
[00:44:30] >> You probably need to think through like
[00:44:32] at a minimum, do you work with Claude at
[00:44:35] work and in personal stuff? Then maybe
[00:44:36] set up a work folder and a personal
[00:44:38] folder. That's it, right? And then I
[00:44:41] think from there, you can just do it
[00:44:44] iteratively over time. And that's what I
[00:44:46] did. Like I literally never sat down and
[00:44:48] just created all these files. I just And
[00:44:50] some of them are just stubs, right?
[00:44:52] They're not that complete. Um but I know
[00:44:55] I'll add to them with time. And then
[00:44:57] this file we're looking at, this
[00:44:58] profile, I never wrote a word of it.
[00:45:00] Every time I have Claude add a context
[00:45:03] file, I say, "What index needs to be
[00:45:05] updated?" And it just figures it out.
[00:45:06] >> Got it. Okay. So maybe like the process
[00:45:09] here is like think about your weekly
[00:45:11] calendar. What's like the most like
[00:45:12] what's taking up most of your time? And
[00:45:14] then and then uh try to you know you
[00:45:16] have Claus as your employee try to get
[00:45:17] it to you know give a bunch of
[00:45:19] instructions backgrounds context have it
[00:45:20] save a bunch of files and then just work
[00:45:22] with it to start doing stuff and then at
[00:45:24] the end of every conversation ask it to
[00:45:26] like add more stuff to context or like
[00:45:29] improve his prompt that that's kind of
[00:45:30] [laughter]
[00:45:31] that's kind of what you do right
[00:45:32] >> yeah okay I think there's two steps to
[00:45:35] this first is I have worked with an
[00:45:38] admin for like 10 years so I'm really
[00:45:40] good at like looking at things that I
[00:45:43] can delegate And for anybody who's ever
[00:45:45] delegated something to another person,
[00:45:47] what makes that work well is to have
[00:45:49] like a good like standard operating
[00:45:53] procedure for the task you're giving
[00:45:54] them, right? It's not you can't just say
[00:45:57] to someone another human like, "Hey, go
[00:45:59] do this thing and have them expect them
[00:46:02] to be able to do it the way that you
[00:46:03] would do it." And so if you want them to
[00:46:04] do it the way that you would do it, you
[00:46:06] have to provide for them like a process
[00:46:09] like here's how I do it. Here's the
[00:46:11] outcome that I want. And so like I do
[00:46:13] this with my admin but I record videos.
[00:46:15] I record a video of how I do things. She
[00:46:18] then looks at the video. She creates
[00:46:20] like a Trello checklist for herself and
[00:46:22] then that becomes like our standard
[00:46:23] operating procedure. So we've been doing
[00:46:25] this for years. And so I'm already good
[00:46:27] at this muscle of like what can I
[00:46:29] delegate? So when I started doing this
[00:46:31] with LLMs, I thought about it as like
[00:46:33] okay well if Claude is just a person on
[00:46:35] my team, how would I delegate to Claude?
[00:46:37] And so I started by literally looking at
[00:46:40] my own Trello board and like what do I
[00:46:41] need to work on today? And then it for
[00:46:44] every task I got in the habit of like
[00:46:46] how can Claude help with this.
[00:46:47] >> Got it. Got it.
[00:46:49] >> And then there's pieces for some tasks
[00:46:51] like I don't want to automate them. I
[00:46:53] enjoy doing them. Like I enjoy writing.
[00:46:54] I don't want Claude to write for me. So
[00:46:56] like I don't want to automate that. So I
[00:46:58] think about like how can Claude augment
[00:47:00] this. What do I do while writing that
[00:47:02] Claude could accelerate? well, research
[00:47:04] and web searches um and like coming up
[00:47:06] with alternative analogies. And then
[00:47:09] there's other tasks like send this
[00:47:12] stupid receipt to my finance system. I
[00:47:14] don't need to ever do that. I could
[00:47:16] automate that. So then I look at like
[00:47:18] what do I have to do to give Claude
[00:47:19] context to be able to automate this
[00:47:21] completely. Um so
[00:47:23] >> okay,
[00:47:24] >> I didn't even start with the things that
[00:47:25] take the most time. I literally just
[00:47:27] forced myself all day, every day, every
[00:47:30] time I do a new task to think about like
[00:47:33] how can Claude help.
[00:47:34] >> Got it. All right, man. That that that
[00:47:36] that's a great tip to end on. I I think.
[00:47:39] [laughter]
[00:47:39] >> All right.
[00:47:39] >> Yeah. Just hire hire $100 employee and
[00:47:42] then uh get it to help on different
[00:47:44] things. Yeah.
[00:47:44] >> Yeah. And I mean, it's funny that I even
[00:47:47] thought twice about upgrading from $20
[00:47:49] to $100. I started on the $20 plan. I
[00:47:52] only had to bump to the $100 plan when I
[00:47:55] was doing both a lot of coding in one
[00:47:58] week and a lot of writing in one week.
[00:48:00] So, it's like I was literally pushing
[00:48:03] hard on Claude for a long time. So, you
[00:48:06] can get pretty far on the $20 plan.
[00:48:08] >> Yeah. Yeah. Yeah. Yeah. And hopefully
[00:48:10] Anthropic gets his limits together, you
[00:48:12] know.
[00:48:12] >> Yeah. [laughter]
[00:48:13] >> So, yeah.
[00:48:14] >> Okay. So, to find your detailed cloud
[00:48:15] code guides, just go to producttalk.org,
[00:48:18] right? Is that the right site? Yeah,
[00:48:20] it's all we can take a look right here.
[00:48:22] It's productt talk.org and it's all like
[00:48:24] all my recent articles. You can see what
[00:48:27] is claude. Stop repeating yourself.
[00:48:30] Probably by the time this episode goes
[00:48:31] out that safety article will be live.
[00:48:34] >> Awesome. I'll I'll definitely read it.
[00:48:36] Yeah, [laughter]
[00:48:37] >> there's a ton here. I'm going to be
[00:48:38] writing a lot more. Like a lot of my
[00:48:40] goal for the next several weeks is just
[00:48:43] to help make Claude code accessible for
[00:48:46] people for nontechnical people and to
[00:48:48] really start to show the power of like
[00:48:50] pair working with Claude. Um so if
[00:48:53] listeners were like excited about this
[00:48:55] episode definitely check out this
[00:48:56] series. It's been a fun to write and I'm
[00:48:59] I'm even going to be hosting Claude code
[00:49:01] office hours. So if you want to even
[00:49:02] come and get help uh I'm going to be
[00:49:05] doing that every month.
[00:49:06] >> Awesome. Awesome. You should should be
[00:49:07] there. You should be Anthropic exposing.
[00:49:09] Yeah, [laughter] that sounds great.
[00:49:11] Yeah. Yeah.
[00:49:11] >> I know. Someone asked me if I was being
[00:49:13] sponsored by Anthropic, and I'm not. Uh
[00:49:16] if I was, I would disclose that. I
[00:49:17] really am just a big fan.
[00:49:19] >> Yeah, I'm a really big fan, too. I'm a
[00:49:20] really big fan of like Capors and the
[00:49:22] team and what they're building and um
[00:49:24] yeah, it's funny because they're they're
[00:49:26] really kind of trying to build towards
[00:49:27] the coding use case, but like you know,
[00:49:29] there's so much more you can do to build
[00:49:30] a really good agent.
[00:49:32] >> Yeah.
[00:49:32] >> Cool. All right, Teresa, thank thanks so
[00:49:34] much for your time.
[00:49:35] >> Thanks for having me. This has been fun.
