[00:00:00] If you think about it, there's like a
[00:00:01] third shift between midnight and 8 a.m.
[00:00:03] roughly, right? That people tend not to
[00:00:06] work because they're sleeping.
[00:00:07] >> Imagine if operations like logistics
[00:00:09] could still run during that shift,
[00:00:11] right?
[00:00:12] >> Um and then same thing, imagine you're a
[00:00:13] field service technician, you need a
[00:00:15] part. Like how amazing would it be if
[00:00:16] the part could just get delivered to
[00:00:18] you? Like that is something that's going
[00:00:20] to be a nice augment to operations. So
[00:00:22] it's interesting because typically when
[00:00:24] you see automation kick in um again
[00:00:26] volume increases, right? Because costs
[00:00:28] come down. there's way more demand out
[00:00:30] there than people realize because
[00:00:31] sometimes you'll say, "Yeah, I could use
[00:00:33] that part, but I don't need to deliver
[00:00:34] it if it's going to cost 50 bucks for
[00:00:35] someone to drive it to me." Yeah. If it
[00:00:37] costs five bucks or or no bucks, like
[00:00:39] how awesome would that be? So, we kind
[00:00:41] of view it as like it will increase the
[00:00:43] speed that the world operates at.
[00:01:01] In this episode, we talk with Sanjit
[00:01:03] Biswas, founder and CEO of Samsara.
[00:01:06] Sanjett formerly founded Moroi and has a
[00:01:08] legendary reputation amongst Sequoia's
[00:01:10] founders. So, I'm excited to welcome him
[00:01:12] today for a conversation about physical
[00:01:14] AI. Samsara is a $20 billion market cap
[00:01:17] public company with sensors deployed in
[00:01:19] streaming data from millions of vehicles
[00:01:21] capturing 90 billion miles annually.
[00:01:23] Sanjett shares his insights about the
[00:01:25] constraints of physical AI from running
[00:01:28] inference on 2 to 10 watt edge devices
[00:01:30] to why the messy diversity of real world
[00:01:32] data is both the biggest challenge and
[00:01:34] opportunity for embodied AI. If you're
[00:01:37] building in robotics or physical AI,
[00:01:39] this conversation offers a rare
[00:01:40] perspective from somebody who's actually
[00:01:42] scaled it. Enjoy the show.
[00:01:46] Sanjit, thank you so much for joining us
[00:01:48] today. you are a legendary Sequoia
[00:01:50] founder and it is a delight to have you
[00:01:52] uh back at Sequoia.
[00:01:53] >> Thanks for having me. It's great to be
[00:01:54] back.
[00:01:55] >> Um I want to start with your background.
[00:01:57] So you you went from MIT's RoofNet
[00:02:00] project to co-founding Moroi through its
[00:02:03] 1.2 billion acquisition and you are now
[00:02:05] the founder and CEO of Samsara, a 23
[00:02:08] billion market cap company um with the
[00:02:11] best ticker on the on the public
[00:02:13] markets. Uh what's what's the through
[00:02:15] line? and tell tell me about your your
[00:02:16] personal passions and and experiences
[00:02:18] and what the through line is between all
[00:02:20] of that.
[00:02:20] >> Yeah, so uh I'm an engineer by
[00:02:22] background. So studied E and CS. Um I
[00:02:25] went to undergrad out here at Stanford,
[00:02:26] went to MIT for grad school and that's
[00:02:28] where we worked on this project called
[00:02:29] roofnet. So the throughine for me has
[00:02:31] been about building cool products, cool
[00:02:33] technologies that have real world impact
[00:02:35] and roofnet this is like over 20 years
[00:02:37] ago. The idea was could you build really
[00:02:40] big wireless networks because at you
[00:02:42] know kind of early 2000s Wi-Fi was not
[00:02:45] mainstream. It was a brand new
[00:02:46] technology. Internet access was just
[00:02:48] becoming mainstream and is still pretty
[00:02:50] expensive. And so we saw this
[00:02:52] opportunity to take Wi-Fi chips and all
[00:02:54] that technology and use it to build
[00:02:56] really big networks. And so we kind of
[00:02:57] had this idea that uh internet access
[00:03:00] should be everywhere, right? It should
[00:03:01] be in the air.
[00:03:02] >> And how would you do that? We need to
[00:03:03] build a big network. So that was
[00:03:04] roofnet. And then with Samsara uh it's a
[00:03:07] bit of a different sort of focus. We
[00:03:08] focus on the world of physical
[00:03:09] operations. So think all the
[00:03:11] infrastructure companies whether it's
[00:03:12] energy utilities, construction,
[00:03:14] logistics like all these real world
[00:03:15] physical industries and the idea has
[00:03:17] been real world impact through things
[00:03:19] like risk reduction, improving
[00:03:20] efficiency, um improving sustainability,
[00:03:23] just using all this data and now AI.
[00:03:25] >> Yeah. Um physical AI feels like it's
[00:03:28] finally going through an inflection
[00:03:29] moment. You've been building Samsara for
[00:03:31] the better part of a decade now. What
[00:03:32] did you see at the time and like how has
[00:03:34] the field changed? Why why now?
[00:03:37] >> Yeah. So, if I rewind 10 years to when
[00:03:39] we were founding the company, we had a
[00:03:41] couple of sort of intuitive bets or
[00:03:43] guesses. And the why now for us at that
[00:03:45] point was connectivity. So, we'd been
[00:03:48] through the Moroi journey and we'd seen
[00:03:50] internet access go from being kind of
[00:03:51] rare and inexpensive to being
[00:03:53] ubiquitous. So, this is 2015 for
[00:03:55] reference.
[00:03:56] >> Um, we saw basically the ability to
[00:03:59] process large amounts of data really
[00:04:01] coming online. So the cloud had matured.
[00:04:03] Um we were seeing the beginnings of the
[00:04:05] GPU wave. Um and if you remember back to
[00:04:08] 2015, Nvidia was a player and they were
[00:04:11] doing a lot of interesting like embedded
[00:04:12] GPUs. So if you picked up a Nintendo
[00:04:14] Switch back then, it had amazing
[00:04:16] graphics, but it fit in your hand. And
[00:04:18] so we saw compute was getting really
[00:04:19] good. And then we saw sensors really
[00:04:21] specifically cameras were getting really
[00:04:23] good because this is probably seven,
[00:04:25] eight years after the iPhone launch. So
[00:04:27] cameras had gotten extraordinary. Um,
[00:04:30] and you combine all these three things
[00:04:31] together. You've got connectivity,
[00:04:32] you've got compute, and you've got
[00:04:33] sensors, cameras. And we said this is
[00:04:36] the sort of like makings for u total sea
[00:04:39] change when it comes to ability to
[00:04:41] process data in real world context.
[00:04:43] >> Wonderful. Okay. I'm excited to nerd out
[00:04:45] more about uh technical questions on the
[00:04:47] frontier of physical AI. Before we get
[00:04:50] into it, maybe can you just say a word
[00:04:51] on Tamsara for our listeners? Um I guess
[00:04:54] how much of the business is you know I
[00:04:56] think of it as very much a having had
[00:04:58] roots in commercial trucking. How much
[00:04:59] of the business is that today and what
[00:05:01] do you see the ultimate vision of
[00:05:02] Samsara being?
[00:05:03] >> Yeah so we really focus on the broad
[00:05:06] world of physical operations. So think
[00:05:07] about all these different kinds of
[00:05:08] industries. Trucking is definitely one
[00:05:10] of them. It's about 20 25% of our
[00:05:12] business. So logistics and and big
[00:05:14] trucks on the road. A lot of our
[00:05:15] business now is related to field service
[00:05:17] and construction. So other big kind of
[00:05:19] frontline industries. Uh but we also are
[00:05:21] starting to do work in like um public
[00:05:23] sector. So we work with local
[00:05:25] governments. We work with student
[00:05:27] transit. So we just signed like the
[00:05:28] largest yellow school bus operator in
[00:05:30] North America which is pretty cool. Um
[00:05:32] and we work in industries like aviation.
[00:05:34] So think about like labor intensive
[00:05:37] asset heavy industries that really power
[00:05:39] the infrastructure of the planet.
[00:05:40] >> Wonderful.
[00:05:41] >> Can I go back to your comment on so at
[00:05:43] the time there was a why now around
[00:05:45] bandwidth compute and cameras.
[00:05:47] >> Yeah. And it sounds like you may not
[00:05:49] have necessarily had a crystal ball on
[00:05:51] what was going to happen with AI.
[00:05:53] >> Yeah.
[00:05:53] >> But you kind of felt like you're on the
[00:05:55] right side of history and that with
[00:05:57] those raw ingredients, you'd be able to
[00:05:58] do increasingly sophisticated stuff over
[00:06:01] time.
[00:06:01] >> Yeah.
[00:06:02] >> Um what I'm curious about I feel like
[00:06:04] there are a lot of founders today who
[00:06:05] are kind of in a similar position where
[00:06:07] nobody has a crystal ball. We don't
[00:06:09] really know what's coming, but you kind
[00:06:11] of know that whatever capabilities
[00:06:12] you're going to have tomorrow are very
[00:06:13] different and better than whatever
[00:06:14] capabilities you have today.
[00:06:16] >> Yeah. So I guess the question is like
[00:06:18] since you kind of had a directional
[00:06:20] sense for where the world was going, how
[00:06:22] did that influence the way you built the
[00:06:24] business? Like was there anything
[00:06:25] specifically you did just kind of in
[00:06:27] anticipation of this inevitable
[00:06:29] direction that the world was going?
[00:06:31] >> Well, actually the historical context is
[00:06:33] important. So our first company Moroi,
[00:06:35] which was uh funded by Sequoia, we were
[00:06:37] domain experts. So we knew a ton about
[00:06:39] networking because that's what we'd been
[00:06:41] working on in terms of our PhD. With
[00:06:42] Samsara, it was kind of the opposite. We
[00:06:44] knew nothing about this domain. Like
[00:06:46] we'd never driven a commercial truck
[00:06:47] before, never worked in a warehouse. And
[00:06:49] so we were sort of eyes open about it.
[00:06:51] What we did have was that intuitive
[00:06:52] sense of the compounding rate of those
[00:06:54] underlying technologies. So we said,
[00:06:56] okay, there's this really interesting
[00:06:58] like problem space, this world of
[00:06:59] physical operations. It's kind of like
[00:07:01] overlooked, especially 10 years ago. No
[00:07:03] one was really talking about
[00:07:04] infrastructure the way they are now.
[00:07:06] >> But there are, you know, things are
[00:07:08] changing very quickly behind the scenes
[00:07:09] in terms of tooling. So that intuition
[00:07:12] is exactly sort of what we were powered
[00:07:14] by and we said even if it's not
[00:07:16] mainstream yet or it's not ready yet
[00:07:19] certainly in 5 to 10 years which is
[00:07:20] about now it will be possible to do this
[00:07:23] stuff. So I think for a lot of the
[00:07:24] current founders it's kind of like if
[00:07:26] you look at AI model capabilities even
[00:07:28] when like you know the chat GPT moment
[00:07:30] happened these models weren't perfect
[00:07:32] they've gotten a lot better in the last
[00:07:34] 2 three years and they're going to get
[00:07:35] even better in the next two to three
[00:07:36] years. I think technical people
[00:07:38] understand that in a way that consumers
[00:07:40] and customers often may not see yet.
[00:07:42] >> So I think you have an embedded systems
[00:07:44] background and you know you're one of
[00:07:46] the unique people that's you know
[00:07:48] operated at the intersection of hard the
[00:07:50] hardware and software worlds. Um I'm
[00:07:52] curious what are the things that make
[00:07:54] building AI in the physical world
[00:07:58] different than you know running AI in
[00:08:00] big data centers?
[00:08:01] >> Uh a couple of things. Well the it it
[00:08:03] actually is a lot of fun. So the
[00:08:04] physical world is very diverse. Um, you
[00:08:06] know, you see a lot of companies now
[00:08:07] working on physical intelligence and
[00:08:09] world models and it's because the
[00:08:11] training data set is really broad and
[00:08:12] vast.
[00:08:13] >> Um, so if you think about our products,
[00:08:15] we have products like dash cams that end
[00:08:17] up on the roads on millions of vehicles.
[00:08:19] They see like 99% of the US roads. It's
[00:08:22] just an incredible data set. You've got
[00:08:24] urban, you've got rural, you've got
[00:08:25] residential, you've got weather. And so,
[00:08:27] uh, we see all these like interesting
[00:08:29] exceptional cases. So, the training data
[00:08:31] is really interesting. and then what we
[00:08:33] can apply all the inference and and
[00:08:35] basically pattern matching to is also
[00:08:37] interesting. So I think that's the most
[00:08:38] fun part. The most challenging part
[00:08:40] though is how messy it is and how
[00:08:42] distributed it is. So um for our
[00:08:45] products it's it's not practical for us
[00:08:47] to just stream all the data to the
[00:08:49] cloud. It would be like a crazy
[00:08:51] bandwidth bill. Um you need pretty
[00:08:53] massive data centers if you think about
[00:08:55] millions of video streams like
[00:08:56] constantly running inference. And so we
[00:08:58] have a much more distributed
[00:09:00] architecture where we actually run in
[00:09:01] the cameras themselves. And that changes
[00:09:04] uh your compute and power footprint. You
[00:09:06] know, we're talking about 2 to 10 watts,
[00:09:09] not like kilowatts, right? Um but you
[00:09:12] can do a lot more because you've got
[00:09:13] millions of them.
[00:09:14] >> H And so what does it like? How do you
[00:09:16] run I'm thinking some of these large
[00:09:18] LLMs, even even the image image models
[00:09:21] are
[00:09:22] >> very large right now that people are
[00:09:23] working with. Are you are you running
[00:09:25] just very bespoke small models on on 2
[00:09:28] to 10 watts? That's that doesn't give
[00:09:29] you much.
[00:09:30] >> It doesn't give you a lot of room and
[00:09:31] that's a fun engineering problem. So um
[00:09:33] if you think about it, these
[00:09:34] state-of-the-art models, they are very
[00:09:35] large. So you're talking about like you
[00:09:38] know hundreds of millions of parameters
[00:09:39] or billions of parameters that is simply
[00:09:41] not possible. So our footprint is much
[00:09:43] more similar to what you can run on like
[00:09:45] your mobile phone, right? Um so it's not
[00:09:47] tiny. It's not a microcontroller. It
[00:09:49] runs Linux. It's got like hundreds of
[00:09:51] megs of memory, maybe gigs. um but it's
[00:09:54] it's not like a big data center right so
[00:09:56] what we tend to do is we will um train
[00:09:59] models in the cloud we'll basically
[00:10:01] distill them down or use teacher models
[00:10:03] so we'll use a big model to basically
[00:10:05] instruct a small model that's really
[00:10:07] designed for our use case because we
[00:10:09] don't need to be able to answer you know
[00:10:11] what the capital France is right like
[00:10:13] that's not something the dash cam has to
[00:10:14] encounter but we do need to be able to
[00:10:16] understand what is the risk profile on
[00:10:18] the road so we train it with the data
[00:10:19] that's relevant for the task
[00:10:21] >> how much of the data you see 99% of US
[00:10:24] highways or US roads. How much of that
[00:10:26] data can you make use of? How much of
[00:10:28] that data do you make use of?
[00:10:30] >> Yeah. Um we can make use of a lot of it
[00:10:33] and u we basically have the ability to
[00:10:34] train over like this entire data set.
[00:10:37] There is a very practical question of
[00:10:38] like okay you run a tokenizer at the
[00:10:40] edge you you send all these to the cloud
[00:10:42] what do you do with it? And what's cool
[00:10:44] about that is what we do with it this
[00:10:46] year is so much more interesting than
[00:10:48] what we could do with it two three years
[00:10:49] ago. So two to three years ago and and
[00:10:52] these products really started around
[00:10:53] this idea of reducing risk. So if you
[00:10:54] think about the problem we're trying to
[00:10:56] solve, it's that you know our operations
[00:10:59] customers they operate on these roads
[00:11:00] every day. It's actually the riskiest
[00:11:02] thing that they do is more so than
[00:11:04] construction or working in oil and gas.
[00:11:06] Driving on the highway getting to and
[00:11:07] from the job site is where they incur
[00:11:09] like most of their like fatality or or
[00:11:11] kind of high severity risk. M
[00:11:14] >> so uh the question is how do you go take
[00:11:16] all these images and tokens and turn it
[00:11:18] into a risk signal right um couple years
[00:11:21] ago we said you know the biggest risk we
[00:11:23] are seeing right now is mobile phone
[00:11:24] usage right like people are on their
[00:11:26] mobile device while driving a big truck
[00:11:28] and that's super risky so we built a
[00:11:30] detector for that
[00:11:31] >> um you do that and you say okay we can
[00:11:33] solve this problem we can detect mobile
[00:11:35] phones what else drives risk um now
[00:11:37] we're seeing things like weather right
[00:11:39] and weather's always been a risk factor
[00:11:40] it's not a brand new one but it's now
[00:11:42] something we can detect using these
[00:11:44] pretty sophisticated models. Training a
[00:11:46] weather detector using like old school
[00:11:49] convolutional networks like an AlexNet
[00:11:51] style model, you would have gotten a lot
[00:11:53] of things wrong. You couldn't tell the
[00:11:54] road conditions. Once you use more
[00:11:56] sophisticated models like the ones we
[00:11:58] have today, you can really figure it
[00:11:59] out. So that's the cool thing is there
[00:12:01] are these unlocks that happen every
[00:12:02] couple years as model capabilities
[00:12:04] increase and our data set increases. So
[00:12:06] these two things like really work in our
[00:12:08] favor. Is there an upcoming unlock that
[00:12:11] you are most looking forward to
[00:12:12] >> uh in terms of our product sad or just
[00:12:14] in general
[00:12:15] >> a new capability that's going to unlock
[00:12:16] some new use case or some new feature
[00:12:18] for your product?
[00:12:20] >> You know I feel like we are seeing just
[00:12:22] such incredible foundational model
[00:12:24] capabilities that are making it possible
[00:12:27] to just inference over huge amounts of
[00:12:29] data. So historically what we did is we
[00:12:31] understood like what was happening in
[00:12:33] the moment right? So like I said mobile
[00:12:34] phone detection or not wearing a seat
[00:12:36] belt or following distance. Now we can
[00:12:38] start to really look over the course of
[00:12:40] a trip and we're not only detecting like
[00:12:43] negative like risky downside events, but
[00:12:45] we can actually detect good behaviors
[00:12:46] too. And I'm really excited about that
[00:12:48] because frontline workers 80 90% of the
[00:12:50] time they're doing a great job. No one's
[00:12:52] able to recognize it because no one sees
[00:12:53] it. So what's awesome is we can now see
[00:12:56] that someone's doing awesome and give
[00:12:58] them a high five or like some kind of
[00:13:00] recognition or kudos that is like making
[00:13:02] people's day and it's a cool like silver
[00:13:05] lining side effect of having all this
[00:13:06] stuff running. So anyway, it's kind of a
[00:13:08] unexpected upside sort of thing. Yeah.
[00:13:11] >> And do you think it'll be video
[00:13:13] reasoning models that sort of empower
[00:13:15] that? I know you can't run a ton you
[00:13:17] can't run giant models at the edge, but
[00:13:19] are you doing stuff server side that
[00:13:22] takes advantage of
[00:13:22] >> LLM? Yeah, I should have mentioned that.
[00:13:24] So um the model's connected. Um we have
[00:13:26] a ton of inference running at the edge.
[00:13:28] is running continuously because when
[00:13:29] you're driving there's like continuous
[00:13:31] risk and then we're taking those tokens
[00:13:33] we're streaming them up and and addition
[00:13:35] you know we have images we have video we
[00:13:37] have other kinds of telemetry um and
[00:13:40] then we can go and run all kinds of
[00:13:41] sophisticated things in the cloud so if
[00:13:43] we need to understand when an accident
[00:13:45] happened what really happened we can run
[00:13:47] a full video language model like like a
[00:13:49] reasoning model essentially in the cloud
[00:13:51] and that can say oh this was actually
[00:13:53] defensive driving and this guy got cut
[00:13:55] off or these were the conditions so that
[00:13:57] is really cool. Um, we couldn't have
[00:13:59] done that 5 years ago.
[00:14:01] >> Do you believe in world models? Loaded
[00:14:03] question.
[00:14:04] >> Um, I do. I'm I'm cautiously optimistic
[00:14:06] about them, but I think you need a
[00:14:08] tremendous amount of data.
[00:14:09] >> Yeah. Are you guys training your own
[00:14:10] world models?
[00:14:12] >> We are not building our own world model.
[00:14:13] Um, and I think it that requires a very
[00:14:16] specific kind of focus, but uh in the
[00:14:18] same way we don't train our own like
[00:14:20] base foundation models, but we are
[00:14:22] looking forward to using them at some
[00:14:23] point.
[00:14:24] >> Yeah. And I imagine you have an
[00:14:25] incredibly rich data set that might be
[00:14:27] useful.
[00:14:28] >> We do. Yeah. We see about 90 billion
[00:14:30] miles on our system every year. So, it's
[00:14:33] a lot of driving.
[00:14:34] >> Yeah. It seems like the sensor footprint
[00:14:37] you've built out is like a tech nerd's
[00:14:39] dream, right? Most people dream of a
[00:14:42] connected world and, you know, you
[00:14:44] should be able to have so much telemetry
[00:14:45] on all these different attributes of the
[00:14:47] physical world. But as far as I can
[00:14:49] tell, you're one of the only companies
[00:14:50] that's really out gone out and, you
[00:14:53] know, put sensors on the physical world
[00:14:55] in a meaning in a really meaningful way.
[00:14:57] >> Why do you think that is? And what's the
[00:15:00] key to actually being able to make that
[00:15:01] dream happen versus have it just be a,
[00:15:03] you know, tech nerds tech nerd's dream?
[00:15:05] >> Yeah, first of all, it it takes uh it
[00:15:08] takes a village to actually get the
[00:15:09] stuff out there. Um, and I think that's
[00:15:11] maybe one other big difference between
[00:15:13] just pure software and physical world.
[00:15:15] Yeah. Is we have to get the products
[00:15:17] installed, so they're installed in
[00:15:19] millions of vehicles. We have to train
[00:15:21] frontline workforces on like what the
[00:15:23] stuff is and what it's doing. Um, and
[00:15:25] then we have to provide value to all
[00:15:26] these customers kind of from day one,
[00:15:28] right? Like they have to get something
[00:15:30] out of it. Um, you combine all this
[00:15:32] together and you get this big footprint.
[00:15:33] But it's been hard because you need
[00:15:35] thousands of people at our scale now to
[00:15:37] do this and to do the change management
[00:15:39] like the installs and all that kind of
[00:15:41] stuff. Um you know there are a few
[00:15:43] companies that have data sets of the
[00:15:44] scale but it's like Tesla and probably
[00:15:46] us right and then Whimo there's
[00:15:48] thousands of Whimos but not millions and
[00:15:50] maybe it will be millions in the future
[00:15:52] but we're not there yet. So that gives
[00:15:54] you a sense of how much effort is just
[00:15:56] like sheer willpower is required to get
[00:15:58] this stuff out there. Speaking of which,
[00:16:00] I um I think there are a lot of founders
[00:16:03] right now who are technical founders
[00:16:05] like yourself
[00:16:07] >> um who've built something cool
[00:16:10] and
[00:16:12] are now encountering this crazy
[00:16:14] supercharged race to scale that the AI
[00:16:18] wave seems to have brought. And so I
[00:16:21] guess the question is you are a
[00:16:22] technical founder.
[00:16:24] I think both Samsara and Moroi have been
[00:16:28] known for go to market execution.
[00:16:30] >> And so maybe the question is like how
[00:16:32] important has go to market execution
[00:16:35] been to your success and as a technical
[00:16:38] founder was it was it obvious to you at
[00:16:42] the beginning that it was going to be
[00:16:43] that important or kind of what was your
[00:16:44] journey like in
[00:16:46] >> in like appreciating the importance of
[00:16:48] go to market execution if that makes
[00:16:50] sense.
[00:16:50] >> Yeah. I'm replaying like 20 years in my
[00:16:51] head really fast. So uh when we started
[00:16:54] Moroi at that point in time like I had
[00:16:57] never sold anything in my life. In fact
[00:16:59] like I
[00:17:00] >> as an engineering nerd like I avoided
[00:17:02] any situation where there was like you
[00:17:04] know you know those like fundraiser you
[00:17:06] have to sell candy bars at school like I
[00:17:08] would like I was like does anyone need a
[00:17:09] website for this thing? Like you just
[00:17:11] like try to find some way out of it. So
[00:17:12] I I really was not like a salesperson in
[00:17:15] terms of background and no one in my
[00:17:16] family had done sales. So it was very
[00:17:18] foreign. Um, the thing that turned me on
[00:17:20] to it was this idea of this is what it
[00:17:22] takes to get the product out there. And
[00:17:24] if the product's not out there, it's not
[00:17:25] having impact. So if you're driven by
[00:17:26] impact, if that's what motivates you,
[00:17:28] it's fun to see people using it, right?
[00:17:30] Um, and then this is what makes us
[00:17:32] sustainable. So with Moroi, we were
[00:17:34] growing the company between 2006, it was
[00:17:36] acquired in 2012. In the middle of that
[00:17:38] was a great financial crisis, right? Um,
[00:17:41] there wasn't a lot of funding at the
[00:17:42] time. Like risk capital was just like
[00:17:44] turned off. So we basically had to make
[00:17:46] the company operate at break even,
[00:17:48] right? or or thereabouts. And that's
[00:17:50] what really convinced us like we have to
[00:17:52] figure out how to have sustainable sales
[00:17:54] execution and a model that's highly
[00:17:56] predictable. And as engineers, we're
[00:17:58] like, hey, this is actually a big
[00:17:59] engineering problem, right?
[00:18:00] >> Um and then that stuck with us with
[00:18:02] Samsara. We're talking about impact at
[00:18:04] scale.
[00:18:05] >> Uh we raised capital along the way, but
[00:18:07] actually we reinvested way more just
[00:18:09] from the revenue of the company, the
[00:18:11] gross margin. So if you look at our
[00:18:12] numbers, we're public now. So you can
[00:18:13] kind of go back through the balance
[00:18:15] sheet. Um, you can see we've invested
[00:18:17] probably close to three billion dollars
[00:18:19] just in getting the stuff out there,
[00:18:21] right? R&D, customer success, all that
[00:18:23] stuff. That is only possible with a lot
[00:18:25] of sales, right? Um, so once you
[00:18:27] understand the why, you can kind of buy
[00:18:29] into it and say, "I'm going to figure
[00:18:30] this out." It was not natural for us,
[00:18:32] but it was a pivot that that ended up
[00:18:35] being something we had to do, and I'm
[00:18:37] really glad we figured it out and have
[00:18:38] been getting better at it each year.
[00:18:40] >> Yeah.
[00:18:41] >> Moro, you were a domain expert. Samsara
[00:18:43] you were not when you started the
[00:18:45] company. Why why go and pick that
[00:18:47] domain?
[00:18:49] >> I think it was curiosity. Um and this is
[00:18:52] a little bit of like you going back to
[00:18:54] sort of curious nerd roots like you just
[00:18:56] find yourself like reading books and
[00:18:57] wondering how stuff works. Um so after
[00:19:00] Moroi we actually didn't have a plan to
[00:19:02] start another company. Uh there was a
[00:19:04] while I thought I was going to go back
[00:19:05] to grad school finish the PhD kind of
[00:19:07] thing. Uh my co-founder John Bickett
[00:19:10] he's like way smarter. He's like that's
[00:19:11] never going to work. But uh you go do
[00:19:14] that and in that period of time I
[00:19:16] realized that academic research is very
[00:19:18] long feedback loop kind of slow cycle
[00:19:20] but there were a lot of other
[00:19:21] interesting problems that caught my
[00:19:22] attention. So I I got interested I think
[00:19:25] in energy at that time. So I was like
[00:19:26] learning about um how the electrical
[00:19:29] grid worked or the time didn't work
[00:19:30] because photovoltaics and renewables
[00:19:32] were coming online. Um I started getting
[00:19:34] curious about nuclear about um
[00:19:36] satellites and things like that. So,
[00:19:38] it's kind of fun to be able to just open
[00:19:39] your mind up to everything when you've
[00:19:41] been like laser focused on one thing.
[00:19:43] >> Yeah.
[00:19:44] >> And then over and over, um, I found
[00:19:46] myself and then John found himself like
[00:19:47] attracted to this world of
[00:19:49] infrastructure. And so it was just
[00:19:50] curiosity about this part of the world
[00:19:52] that felt pretty overlooked.
[00:19:54] >> Really cool. What do you think of
[00:19:56] autonomy? And that might be a loaded
[00:19:58] question. Yeah. But, you know, I two
[00:20:00] years ago I avoided getting in wayos.
[00:20:02] Now I don't think now I don't think
[00:20:03] twice. I feel safer in a Whimo than not
[00:20:05] in one. Um what's your what's your point
[00:20:08] of view?
[00:20:08] >> Um super excited about it. Very bullish.
[00:20:10] I think uh it's been a long time coming.
[00:20:13] When I was in undergrad at Stanford,
[00:20:14] they were doing the first like DARPA
[00:20:16] Grand Challenge cars. So this is like 20
[00:20:18] plus years ago now.
[00:20:19] >> And like you said, Whimos have gone from
[00:20:21] kind of like prototype test to like I
[00:20:23] prefer Whimo, right? It's super
[00:20:25] consistent.
[00:20:26] >> Um you know, there's lots of things to
[00:20:27] like about it. So our view on it is
[00:20:30] autonomy happens and it actually
[00:20:31] increases the operational intensity of
[00:20:33] the world, right? So, if you think about
[00:20:35] it, there's like a third shift between
[00:20:37] midnight and 8 a.m. roughly, right? That
[00:20:39] people tend not to work because they're
[00:20:41] sleeping. Imagine if operations like
[00:20:44] logistics could still run during that
[00:20:45] shift, right?
[00:20:46] >> Um, and then same thing, imagine you're
[00:20:48] a field service technician, you need a
[00:20:50] part, like how amazing would it be if
[00:20:51] the part could just get delivered to
[00:20:52] you. Like that is something that's going
[00:20:54] to be a nice augment to operations. So,
[00:20:57] we're a fan of it. Um, our view on it is
[00:20:59] we think it's an and not not an or
[00:21:01] exclusive. Um, and it's it's interesting
[00:21:04] because typically when you see
[00:21:05] automation kick in, um, again, volume
[00:21:07] increases, right? Because costs come
[00:21:09] down, there's way more demand out there
[00:21:11] than people realize because sometimes
[00:21:12] you'll say, "Yeah, I could use that
[00:21:14] part, but I don't need to deliver it if
[00:21:15] it's going to cost 50 bucks for someone
[00:21:17] to drive it to me." Yeah. If it costs
[00:21:18] five bucks or or no bucks, like how
[00:21:20] awesome would that be? So, we kind of
[00:21:22] view it as like it will increase the
[00:21:24] speed that the world operates at.
[00:21:25] >> You think it's happen on roads only or
[00:21:27] you have customers with warehouses and
[00:21:29] forklifts and all the above? like you
[00:21:31] think autonomy will hit all those
[00:21:32] sectors.
[00:21:32] >> So I think autonomy already hit the
[00:21:34] warehouse. Um we have a lot of customers
[00:21:36] with big like you know logistics
[00:21:38] warehouses and really about 10 years ago
[00:21:40] they started getting automated in a
[00:21:42] meaningful way and it's pretty rare for
[00:21:44] me to go into like a um heavily you know
[00:21:48] industrialized environment without
[00:21:49] seeing automation. And that's everything
[00:21:51] from like lift systems to big arms
[00:21:53] moving things.
[00:21:54] >> And it actually is welcomed by the
[00:21:56] people in the warehouse because it helps
[00:21:57] reduce injury. So if you think about it,
[00:21:59] frontline workers are putting themselves
[00:22:01] at risk when they do their job every
[00:22:02] day. Yeah. It it is not a great outcome
[00:22:05] to get hurt lifting a pallet or, you
[00:22:07] know, doing something like that. So that
[00:22:09] is, I think, a good sort of um preview
[00:22:12] of what we're going to see out on the
[00:22:13] road. And then I think after that
[00:22:14] there's a construction site and job
[00:22:16] site.
[00:22:16] >> Yeah. Humanoids, yes or no?
[00:22:19] >> Uh cautiously optimistic. Little bit
[00:22:21] scary. I won't lie. They they feel like
[00:22:23] they're in that kind of creepy uncanny
[00:22:25] valley like when you see them walking
[00:22:26] around without heads or or hands or
[00:22:28] something. Um
[00:22:29] >> have you seen Neo for
[00:22:30] >> I have that that's a friendly one. Yeah.
[00:22:32] Um but I I think uh it's it reminds me
[00:22:35] of where self-driving was about 10 years
[00:22:37] ago. So probably not a tomorrow but it
[00:22:39] does feel inevitable. So as the
[00:22:41] capabilities increase uh it's going to
[00:22:43] be really exciting.
[00:22:44] >> Yeah.
[00:22:44] >> How does the role that Samsara plays in
[00:22:46] the world change as we have more and
[00:22:48] more autonomy over time? Well, I kind of
[00:22:51] think of it as digital transformation.
[00:22:53] So, if you zoom way out, that's what
[00:22:54] customers are are excited about is how
[00:22:56] do we digitize these operations that
[00:22:58] have been around 50, 100 years in some
[00:23:00] cases.
[00:23:01] >> And most of our customers, they welcome
[00:23:03] new technology. So, they adopted
[00:23:05] computers for, you know, route planning
[00:23:07] like in the 1970s or something like
[00:23:09] that. So, they're not against
[00:23:10] technology. It's is it going to help? Is
[00:23:12] it going to be relevant? So our take is
[00:23:15] you're going to want like a platform to
[00:23:17] see all of your operations for all of
[00:23:18] these different operations to interact.
[00:23:20] So you can see your frontline workers,
[00:23:22] you could see all your vehicles, you
[00:23:24] could see your assets, know what needs
[00:23:26] maintenance. All of these problems will
[00:23:27] will be evergreen. You're going to want
[00:23:29] to maintain your assets like 20, 30
[00:23:31] years from now. Maybe they're robots and
[00:23:33] maybe they move on their own, but they
[00:23:34] still need maintenance, for example. Um,
[00:23:36] and then same thing when you've got
[00:23:38] customerf facing or end customerf facing
[00:23:40] teams, you're still going to need to
[00:23:41] orchestrate hopefully thousands of
[00:23:44] people, right? And they may have help
[00:23:45] from robots and humanoids and all kinds
[00:23:48] of stuff behind the scenes, but how do
[00:23:49] you kind of run the entire operation? So
[00:23:51] that's what we focus on is the big
[00:23:53] picture as opposed to any specific
[00:23:55] product or technology.
[00:23:56] >> How do you see the future of humans and
[00:23:59] AI interacting in the physical world and
[00:24:01] in the industries that you serve?
[00:24:04] Well, I think they're getting closer and
[00:24:05] closer. So, 10 years ago when we started
[00:24:08] Simsara, most of our customers did run
[00:24:10] on a lot of like pen and paper process.
[00:24:12] Like 2015, it's it's not the distant
[00:24:15] past, right? Like it really has been a
[00:24:17] change that they've gone from pen and
[00:24:18] paper to apps. I think as AI kicks in,
[00:24:21] you see many of them like using um voice
[00:24:25] bots for a freight brokerage, right?
[00:24:26] Like that's a brand new phenomenon
[00:24:28] really in the last year
[00:24:29] >> and they've taken to it very quickly.
[00:24:31] It's automating tasks. So I kind of
[00:24:33] think of it as where are there where is
[00:24:34] there high task intensity a lot of like
[00:24:36] repetitive task work and can AI help?
[00:24:39] Absolutely. So that's where we're seeing
[00:24:40] like very high rates of adoption. Um I
[00:24:43] think the stuff that's not changing at
[00:24:44] least not yet is the physical work
[00:24:46] itself is still being done by people
[00:24:48] because it requires a lot of exception
[00:24:50] handling. So construction is a great
[00:24:51] example. So much diversity in
[00:24:53] construction. Um we are not to the point
[00:24:55] where you can automate it the way you
[00:24:57] could automate like car manufacturing
[00:24:59] for example. Do you think AI is, you
[00:25:01] know, you mentioned it's something that
[00:25:03] prevents risky behavior in humans? Um,
[00:25:06] are you also seeing it kind of coach
[00:25:08] humans in these operational environments
[00:25:10] to actually perform better?
[00:25:12] >> Yeah. So, um, you know, and first just
[00:25:15] thinking about risk, coaching makes a
[00:25:16] big difference. So, there's risk
[00:25:18] detection like you know, please put down
[00:25:20] your mobile phone, but then if it's a
[00:25:22] habit of yours, um, we actually want to
[00:25:24] coach you to help break the habit,
[00:25:26] right? And um if you kind of look at the
[00:25:28] impact we're able to have with
[00:25:29] customers, we often reduce risk like by
[00:25:32] 75%. So you know threequarters of the
[00:25:35] risk comes out of the system maybe half
[00:25:37] of that can come from the automated like
[00:25:39] in the- moment inc cab alert and then
[00:25:41] the other half comes from coaching and
[00:25:43] then that same coaching can be applied
[00:25:45] to like fuel efficiency. You can
[00:25:46] actually train drivers to operate heavy
[00:25:49] equipment in really smart ways and you
[00:25:51] can gamify it, right? So that's the kind
[00:25:53] of like cool opportunity that AI has is
[00:25:55] process just enormous amounts of data,
[00:25:57] more data than any human could do. You
[00:25:59] look at patterns across thousands or
[00:26:01] millions of vehicles and then turn it
[00:26:03] into actionable insight. That's
[00:26:04] coaching. Um so you can apply it to
[00:26:06] safety, you can apply it to efficiency.
[00:26:08] It's it's pretty cool.
[00:26:09] >> What's the organizing principle of your
[00:26:11] uh product portfolio? You started from
[00:26:13] dash cams, it's expanded out from there.
[00:26:15] Yeah.
[00:26:15] >> Maybe just tell us the history of how
[00:26:17] the product portfolio has expanded and
[00:26:18] and how you see the future.
[00:26:20] >> Yeah. So we actually started with GPS
[00:26:22] tracking or telematics. So um 2015 dash
[00:26:25] cams were not quite viable yet. Um but
[00:26:28] >> because of the cost or
[00:26:29] >> um yeah cost and both like the back haul
[00:26:32] cost of bandwidth but also uh the cost
[00:26:35] of the cameras and things like that. But
[00:26:37] what was surprising to us was in 2015
[00:26:40] most of the operational environments we
[00:26:42] went into no one had any idea where
[00:26:44] their field teams were. Not in real
[00:26:46] time. And there was this like disconnect
[00:26:48] because Uber and Door Dash had started
[00:26:50] to happen, right? And so it was weird.
[00:26:52] The gig economy had real-time tracking,
[00:26:54] but then like the logistics, like long
[00:26:57] haul logistics economy was still getting
[00:26:59] like breadcrumbs like every 10 to I
[00:27:01] think it was like 5 to 15 minutes. And
[00:27:03] uh this probably predates most of the
[00:27:05] people who listen to to the show, but um
[00:27:08] there was this platform Map Quest that
[00:27:09] predated like Google Maps, right? So
[00:27:10] late '9s Map Quest, like vintage map,
[00:27:13] right?
[00:27:14] >> Sony wasn't around that. you'd have to
[00:27:15] you'd have to print out the map quest
[00:27:17] directions and then take your piece of
[00:27:18] paper to figure out where you were going
[00:27:20] >> and it was this kind of like grainy it
[00:27:22] looked like you know Minecraft level
[00:27:23] graphics. Um the the amazing part was
[00:27:26] our customers now back then were using
[00:27:29] Map Quest printouts and their system for
[00:27:32] uh GPS tracking was built on top of Map
[00:27:34] Quest. So I would go on site and I would
[00:27:36] say whoa we can help with this. So that
[00:27:38] was product number one was GPS tracking.
[00:27:40] Um that got uh that basically got us off
[00:27:43] the ground and and got us into
[00:27:44] customers. And from there we started
[00:27:47] figuring out well really the bigger
[00:27:49] challenge for them was managing risk
[00:27:51] because at that point in time it was
[00:27:53] mid2010s. People did have phones in
[00:27:54] their pockets and um they actually asked
[00:27:57] us we're getting into a lot of
[00:27:58] accidents. Do you have a dash cam you
[00:28:00] recommend that works well with your
[00:28:01] system?
[00:28:02] >> So we said if we built one for you would
[00:28:04] you use it? And they said yeah
[00:28:04] absolutely. So John, my co-founder,
[00:28:06] remember he went to like Amazon, ordered
[00:28:09] like a webcam, plugged it into the USB
[00:28:11] port, and like over the weekend wrote
[00:28:12] some code to get a basic webcam working.
[00:28:15] We brought it back to the customers the
[00:28:16] next week, they tried it, they loved it,
[00:28:18] and then we were watching the videos
[00:28:20] with them, and you could see as people
[00:28:22] were getting to accidents, they like had
[00:28:23] their phone out, right?
[00:28:25] >> And so we said, could we build a
[00:28:26] detection for that? So that's where the
[00:28:28] AI part of the dash cam came from. It's
[00:28:29] very iterative. Um, and that has now
[00:28:32] become our largest product, but it's
[00:28:34] sold with the the first product. So, you
[00:28:36] asked about the the kind of portfolio
[00:28:38] strategy. It's concentric circles. It's
[00:28:40] keep doing what we started with. Um,
[00:28:42] core use case, adjacent use case. What
[00:28:44] else can we do? What else can we do?
[00:28:45] What else can we do? And now we have
[00:28:47] about 10 products out there.
[00:28:49] >> Really cool. You mentioned kind of the
[00:28:50] back haul and and network bandwidth
[00:28:52] being a binding constraint. I'm curious
[00:28:54] if you think the growing adoption of
[00:28:57] Starlink and just you know internet
[00:28:58] everywhere is going to change what it's
[00:29:00] possible to do in the physical world.
[00:29:02] >> Um absolutely. So we started Samsara
[00:29:06] right around the 3G 4G transition and
[00:29:08] the unlock was actually um YouTube
[00:29:11] right. So if you remember 2015 everyone
[00:29:14] was like starting to watch YouTube and
[00:29:15] baseball games and stuff on their phone.
[00:29:17] That drove data consumption way up on
[00:29:19] the carrier. the marginal cost per
[00:29:20] gigabyte came way down and we were able
[00:29:23] to piggyback on that right and so that
[00:29:25] was really cool. I think something
[00:29:27] similar is happening now not just with
[00:29:29] 5G which is like the networks have
[00:29:30] invested even more. Yeah.
[00:29:32] >> Um but now with satellite right like the
[00:29:34] cost of building Starlink is enormous
[00:29:36] like I don't know how much is being
[00:29:38] spent on it's like many tens of billions
[00:29:40] right and launch capacity and know so on
[00:29:42] >> but the marginal cost to add another
[00:29:44] device to Starlink is pretty low right
[00:29:46] and that's like the cost for any network
[00:29:48] effect. Um so we're excited about that
[00:29:50] because it'll help us get that last like
[00:29:52] 1% of coverage. Um, and a lot of our
[00:29:55] customers are in super remote rural
[00:29:57] areas. Um, like we have a lot of
[00:29:58] customers in energy like oil and gas.
[00:30:00] Yeah.
[00:30:00] >> There there are no roads where they
[00:30:02] operate and so there's not that much
[00:30:04] cellular coverage either.
[00:30:05] >> Do you think that does away with some of
[00:30:06] the constraints of running AI on the
[00:30:08] edge? Uh, meaning like today you can
[00:30:11] only use some percentage of you can only
[00:30:13] stream back some percentage of data and
[00:30:14] you do a lot of onboard compute.
[00:30:16] >> Yeah. Yeah.
[00:30:17] >> In a world of just internet everywhere
[00:30:18] where it's just a lot faster and cheaper
[00:30:20] to to send all data back and forth,
[00:30:23] could you be doing a lot of it server
[00:30:24] side and could you be doing a lot more?
[00:30:26] >> You could do more of it, but it's funny
[00:30:28] how like when stuff gets cheaper, you
[00:30:31] find a way to do more, right? And so
[00:30:33] when I think it's like a compression
[00:30:34] problem, right? Like and if the workload
[00:30:37] was static, like if you were just trying
[00:30:39] to get GPS data into the cloud, yes,
[00:30:41] just stream it all, right? Like it's not
[00:30:42] a big deal. If you're trying to get one
[00:30:44] frame per second video from an outward
[00:30:46] facing camera in the cloud, no problem.
[00:30:47] But if you want HD video from a 360 view
[00:30:50] of a truck, like eight cameras,
[00:30:52] >> that's a lot of video. Um, and then same
[00:30:55] thing if you want it with all the other
[00:30:56] telemetry that we get, it becomes pretty
[00:30:58] big. So I think you could potentially do
[00:31:01] it.
[00:31:01] >> Um, but if you can push some of that to
[00:31:04] the edge and and kind of like compress
[00:31:05] it down, everyone benefits from it. H do
[00:31:08] you think controls and autonomy could
[00:31:11] ultimately be running in the cloud or
[00:31:12] you think that's something people always
[00:31:14] want to run on device?
[00:31:15] >> That one I think you're probably going
[00:31:18] to see edge compute for a long time. Um
[00:31:20] and actually if we kind of go a little
[00:31:22] technical for a second, one of the
[00:31:23] challenges there has been around power
[00:31:25] and compute and cost, right? So if you
[00:31:26] think about like a Tesla full
[00:31:28] self-driving computer, it's a couple
[00:31:29] thousand bucks. It takes many hundreds
[00:31:32] of watts of energy and they're like the
[00:31:34] first company to be making it really
[00:31:35] practical at at scale. Whimo's probably
[00:31:38] a bit more.
[00:31:39] >> Um, and so I do think that we will
[00:31:41] continue to see those sorts of
[00:31:42] approaches because safety is like such a
[00:31:45] big deal. Like you've got humans in the
[00:31:47] cab, you've got humans on the road. Um,
[00:31:49] you don't want like, you know, a network
[00:31:51] outage to like affect, you know,
[00:31:53] people's lives.
[00:31:54] >> Yeah. If we're sitting here in 2030,
[00:31:56] what do you think is the biggest way
[00:31:57] that
[00:31:58] >> AI has transformed the physical world
[00:32:00] and physical operations?
[00:32:02] >> I think a couple of thoughts. One is
[00:32:04] we're pretty early, right? right? We're
[00:32:05] at the end of 2025. The sort of AI
[00:32:09] adoption curve in physical operations,
[00:32:11] we're still at the base of it.
[00:32:12] >> And so by 2030, I think we'll have run
[00:32:14] up the curve where be much more
[00:32:16] mainstream in the same way that like
[00:32:18] using apps is much more mainstream now
[00:32:20] than it was 5 10 years ago. Um so I
[00:32:23] think you'll see the current
[00:32:24] technologies basically experience a lot
[00:32:26] more diffusion like get out there. I
[00:32:27] think we're going to see net new
[00:32:29] technologies. Like I'm super excited
[00:32:30] about augmented reality and wearables.
[00:32:32] Like that's going to make a huge
[00:32:34] difference to frontline workforces where
[00:32:35] they have to have their hands free
[00:32:37] >> and it brings AI like into their ear. A
[00:32:39] lot of folks have AirPods in, right? Um
[00:32:41] but having like sort of visual feedback,
[00:32:43] being able to run like a VLM to
[00:32:46] understand what's going on in the
[00:32:47] environment that will be possible in
[00:32:49] 2030. It's not quite possible yet, but
[00:32:51] you can just feel it. It's like right on
[00:32:53] the cusp.
[00:32:54] >> Maybe it'll be glasses. It'll maybe
[00:32:56] it'll be some of these new devices that
[00:32:58] are under the wraps that that probably
[00:33:00] communicate with. Yeah.
[00:33:01] >> What's your favorite personal use of AI?
[00:33:04] >> Personal use of AI.
[00:33:06] >> Um well, I love the the sort of voice
[00:33:08] models like I talk to AI like whenever
[00:33:10] I'm driving to or from work like I'm I'm
[00:33:12] chatting with it and it's not always
[00:33:14] about anything specific like it's kind
[00:33:16] of whatever's on my mind. So, I love
[00:33:17] that.
[00:33:18] >> Um I've become a big fan of like chat
[00:33:21] GPT pulse for example. like it's just
[00:33:23] cool that it tells you about for me
[00:33:25] events that are happening in the Bay
[00:33:26] Area. I've got three kids stuff it kind
[00:33:29] of knows its interest, right? So that
[00:33:30] the whole idea that AI could um know you
[00:33:34] better than you to some extent is really
[00:33:36] profound.
[00:33:36] >> Um so I love that on the personal side
[00:33:38] it kind of exposes us new experiences
[00:33:40] that we wouldn't have known about like
[00:33:41] you know a music performance or
[00:33:44] something like that that my kids would
[00:33:45] like.
[00:33:45] >> Yeah. Yeah. How much of the value that
[00:33:47] you give customers do you think is
[00:33:49] thanks to AI versus thanks to all the
[00:33:51] other technology that you're building?
[00:33:54] >> It's an interesting question. Um, we
[00:33:57] don't really like split it out because
[00:33:59] like there's value in the data, but if
[00:34:01] no one looks at the data, it it doesn't
[00:34:03] have impact, right? So, one of the
[00:34:05] things we've heard from customers is
[00:34:07] this concern about data overload. Like
[00:34:09] if you have sensor streams from every
[00:34:11] vehicle and every frontline worker and
[00:34:13] every asset, what do you do with it all?
[00:34:14] Right? And so AI is pretty awesome in
[00:34:17] terms of really helping just distill
[00:34:19] that down to something actionable. So
[00:34:21] that's why I don't think you can like
[00:34:22] split the two apart anymore. Um but it's
[00:34:25] transformative. It's gamechanging. And I
[00:34:27] spent a lot of time on the road. Like
[00:34:28] last week I was in um Texas, like all
[00:34:30] over um big food distributor, big oil
[00:34:33] and gas company. Uh spent time with like
[00:34:35] the Home Depot. And it's just cool
[00:34:37] hearing how they're using the data in
[00:34:39] such creative ways and um ones that they
[00:34:42] didn't have on their sort of uh roadmap
[00:34:44] when they started with us, but they're
[00:34:45] like, "Hey, if we can use this data to
[00:34:48] help do time card punches, right? Like
[00:34:50] get someone started on their shift and
[00:34:51] they don't have to walk to the office,
[00:34:53] that's awesome." Or if we can share this
[00:34:55] data with our end customer and let them
[00:34:57] know we're almost there or we're
[00:34:58] delayed, that's pretty cool. So it's
[00:35:00] really neat to see these emergent use
[00:35:01] cases.
[00:35:02] >> Really cool. It's it's great to dream on
[00:35:04] all the way that AI can kind of seep
[00:35:06] into all these different workflows and
[00:35:08] everyday lives.
[00:35:09] >> Yeah. And it's never any one thing.
[00:35:10] That's what I love about this is like
[00:35:12] every quarter we get exposed to some new
[00:35:15] use case. And a lot of it is um just you
[00:35:18] spend time with the customer, you
[00:35:20] understand their operation and then you
[00:35:21] come up with like hey if we did that
[00:35:23] would like would a voice bot that made
[00:35:26] uh ETA delivery phone calls be useful to
[00:35:28] you?
[00:35:28] >> And many of our customers don't even
[00:35:30] know that's possible. They've never
[00:35:40] >> curious and your point of view on you
[00:35:43] know there's so much talk of us versus
[00:35:46] China geopolitics and our industrial
[00:35:48] base really needs to catch up or
[00:35:50] robotics or manufacturing or physical AI
[00:35:53] really needs to catch up.
[00:35:54] >> I'm curious if you've seen that actually
[00:35:56] accelerate customer conversations or
[00:35:58] have an impact on your business in any
[00:35:59] way.
[00:36:00] not in my customer conversations. I do
[00:36:03] think there's this like palpable sense
[00:36:04] of we need to modernize and like how do
[00:36:06] we how do we just rethink the way the
[00:36:09] infrastructure runs. So many of our
[00:36:11] customers are involved in data center
[00:36:13] buildouts right now. Um they're the
[00:36:14] energy utility, they're the construction
[00:36:16] company like there's a lot going on
[00:36:17] there and I think that has everyone
[00:36:19] thinking okay what does this mean for us
[00:36:22] and like what should be different about
[00:36:23] our business? So there's a lot of
[00:36:25] introspection going on. I haven't gotten
[00:36:26] the sense it's like US versus China, but
[00:36:29] it's more of like could we do this
[00:36:30] differently now? We're like firmly in
[00:36:32] the 21st century, right? Like it's what
[00:36:34] should be different now than the way
[00:36:36] that like you know previous generations
[00:36:37] ran these operations?
[00:36:39] >> Wonderful.
[00:36:40] >> You've been a multi-time legendary
[00:36:43] founder. Uh any advice for for young
[00:36:45] technical founders who are out building
[00:36:47] an AI right now?
[00:36:49] >> I think it's an amazing time to build
[00:36:51] whether you've done this before or
[00:36:53] you're starting it for the first time.
[00:36:54] like
[00:36:55] >> just the tools that are available um
[00:36:58] it's incredible and like to some extent
[00:37:00] um you know everything's getting
[00:37:02] magnified or amplified right so I think
[00:37:05] about whether it's codecs or cursor or
[00:37:08] all these like automated coding tools if
[00:37:11] you have an idea now you can like sort
[00:37:13] of manifest it into something real so
[00:37:15] much more easily than when we started
[00:37:17] Samar even when we started Moroi like
[00:37:19] back then we were like racking ser we'd
[00:37:21] like buy servers from Dell and like take
[00:37:23] them to the data center and set Like can
[00:37:24] you imagine? It's just like how slow
[00:37:26] that feels now.
[00:37:26] >> I can't even imagine that.
[00:37:27] >> It's actually hard to imagine. And but
[00:37:29] that is happening and we will look back
[00:37:31] 10 years from now and say can you
[00:37:33] believe we did X, right? And I don't
[00:37:34] even know what X is but it will feel so
[00:37:37] different. So it's fun to be on these
[00:37:38] like exponential curves and the best
[00:37:41] place to be on that is to be building,
[00:37:42] right? Yeah.
[00:37:43] >> Really cool. Thank you so much for
[00:37:45] taking the time to share your story and
[00:37:46] what you all are up to on the AI side at
[00:37:48] Samsara.
[00:37:49] >> Thanks. Thanks for having me.
