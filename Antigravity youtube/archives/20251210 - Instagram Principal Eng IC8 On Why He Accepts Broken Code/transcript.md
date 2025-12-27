[00:00:00] Even if I see your diff is going to blow
[00:00:01] up production.
[00:00:03] >> I will I will comment on it and be like
[00:00:05] this is going to blow up production and
[00:00:07] then accept it and be like, "Yeah, make
[00:00:09] sure you fix that first, right?" I've
[00:00:10] never had a case where someone's like
[00:00:12] landed it cuz like people put up diffs
[00:00:14] and like 5 minutes later it's like stamp
[00:00:15] on me and they're like, "What the hell
[00:00:16] is going on?" [laughter] And that's a
[00:00:18] lot cuz I'm on top of it. But also
[00:00:19] because I have this philosophy on like
[00:00:21] diff reviews and risk where if I don't
[00:00:23] think the diff is risky, right? You're
[00:00:25] getting a very rudimentary review and
[00:00:26] like basically you can put that code in
[00:00:29] like so if it's like gated, it's not on
[00:00:32] a core system, right? These things then
[00:00:34] you're going to just get a very high
[00:00:36] level diff and then basically I'm just
[00:00:38] like trusting you.
[00:00:39] >> So you're saying you you modulate your
[00:00:42] level of time investment based on how
[00:00:44] risky the diff is
[00:00:46] >> based on how risky the diff is, right?
[00:00:47] So if you're rewriting it, right, we're
[00:00:49] it it's all gated right now and we just
[00:00:51] want the highle trunk architecture to be
[00:00:53] correct. If you're working on like some
[00:00:54] child component or something, it's like
[00:00:57] cool, it's gated. It's not critical to
[00:00:59] the system. Like
[00:01:01] >> yeah, I'm trusting you to do whatever
[00:01:03] you need to do over there.
[00:01:04] >> So you'll just stamp it stamp stamp it
[00:01:06] let it. Yeah.
[00:01:07] >> Some people view quality different view
[00:01:09] as a uh like an important thing rather
[00:01:13] than just stamping. So do you ever get
[00:01:15] push back on? This is my controversial
[00:01:17] one for sure. So yeah, so I I think that
[00:01:20] is correct for like the the trunk of the
[00:01:22] system, the core core parts of the
[00:01:24] system or anything that's already live
[00:01:25] in prod like is going to get pretty
[00:01:28] thorough review. Yeah, if it's not live
[00:01:30] and prod and it is one of these sub like
[00:01:33] sub parts of the system or less critical
[00:01:35] things like I'll still skim it to make
[00:01:37] sure you didn't do anything like
[00:01:38] absolutely crazy like introduce like I
[00:01:40] don't know security issues or you know
[00:01:42] start mining crypto on our servers or
[00:01:45] something
[00:01:46] >> but uh yeah I'll just like let let that
[00:01:49] let that fly in.
[00:01:51] >> Yeah, I I mean it makes sense. So you're
[00:01:53] basically trading off speed for I guess
[00:01:56] quality, but it's not dumb quality. It's
[00:02:00] like these are places where it makes
[00:02:01] sense to make the trade-off
[00:02:03] >> where you make Yeah. So you can have
[00:02:04] like lower quality components for like
[00:02:06] these the child the child parts of the
[00:02:09] system, right? Or the leaf parts of the
[00:02:10] system. And also these parts are like
[00:02:12] generally easier to unit test.
[00:02:14] >> If they do fail, they only blow up like
[00:02:16] a small part of it, right?
[00:02:18] >> Just a little blow up.
[00:02:19] >> Just a little part of it. If it is badly
[00:02:21] architected, it's only on this like tiny
[00:02:24] part of the system. It's not impacting,
[00:02:26] you know, hundreds of engineers. Maybe
[00:02:27] it impacts a couple and someone one day
[00:02:29] is like, "What the hell's up with this?"
[00:02:31] >> Doesn't take a long time to rewrite.
[00:02:33] Right. Right.
[00:02:33] >> If you mess up the architecture in the
[00:02:34] core trunk, probably takes like hundreds
[00:02:36] of people a long time to like fix. Have
[00:02:38] you ever had someone I remember early in
[00:02:40] my career I was all about speed and I
[00:02:45] was approving some diffs and then
[00:02:47] someone would come back to me and say
[00:02:49] why'd you approve this that was too
[00:02:51] >> you know like let's slow down a little
[00:02:53] bit on this
[00:02:54] >> oh they get some feedback or someone
[00:02:55] says hey
[00:02:57] >> you know calm down like this defin this
[00:02:59] definitely happens actually interesting
[00:03:00] thing so teach the people close to me in
[00:03:03] my teams that like hey it's okay buy
[00:03:07] stamp your diff to put it back in review
[00:03:10] again if you actually need deeper review
[00:03:13] >> or like flag it flag it in the summary
[00:03:15] or the test plan like or comment on it
[00:03:17] like hey I'm actually looking for a deep
[00:03:19] review on this if you know that's how
[00:03:21] our team operates now and this is
[00:03:22] actually really good because I might
[00:03:24] have thought it's like a child part of
[00:03:26] the system and maybe it is still a child
[00:03:27] part of the system but they've thought
[00:03:29] hey this is like could be like more
[00:03:31] performant or like I actually want you
[00:03:33] to double check this
[00:03:34] >> uh so then we use that signal to be like
[00:03:36] okay this person actually wants thing.
[00:03:38] So if I missed it, even if they put a
[00:03:40] comment on it, they'll throw it back
[00:03:41] into review and like be like need real
[00:03:44] review or something like that cuz they
[00:03:45] knew they knew what happened.
[00:03:47] >> Yeah. Yeah. Yeah.
[00:03:48] >> Yeah. I see. That makes sense.
[00:03:50] >> But yeah, there's definitely this is not
[00:03:51] the philosophy of everyone at Meta,
[00:03:53] right? Like we most people it's like
[00:03:55] >> quality high quality for everything.
[00:03:57] >> Yeah. And it depends on the system
[00:03:59] though.
[00:03:59] >> Depends on the system. Also depends on
[00:04:01] like this is like trust you build on
[00:04:02] your team too, right? If you're new on
[00:04:03] the team
[00:04:04] >> probably not going to get this treatment
[00:04:05] for the first couple of weeks. Yeah.
[00:04:06] Yeah.
[00:04:07] >> Although I do want to defer to like how
[00:04:09] do I accept this diff, not how do I
[00:04:11] reject this diff,
[00:04:12] >> which I think is an important philosophy
[00:04:14] to have.
[00:04:16] >> Why is that?
[00:04:16] >> Yeah.
[00:04:17] >> Uh cuz like I'm not trying to like knit
[00:04:19] your code and get you to write it the
[00:04:21] exact way I would write it, right? I'm
[00:04:23] trying to be like, okay, what is
[00:04:24] absolutely blocking this thing from
[00:04:26] going to going to production? Like big
[00:04:29] highle architecture things like I don't
[00:04:32] know some critical bugs like is it going
[00:04:34] to blow up prod right? not like write it
[00:04:36] exactly the way I would write it.
[00:04:38] >> Right. I think that takes a while to get
[00:04:40] to too, right? Like more senior
[00:04:41] engineers usually become amendable to
[00:04:43] this.
[00:04:44] >> Yeah.
[00:04:44] >> But when you're in Yeah. When you're
[00:04:46] like in the first 5 years of your
[00:04:47] career, maybe you've only seen a few
[00:04:48] ways of writing it, right? So you want
[00:04:50] people to write it that exact way.
[00:04:52] >> Yeah. Yeah. Definitely. I I think when
[00:04:55] you're working in a team where there's
[00:04:57] high trust and you get to the point
[00:04:58] where people
[00:05:00] >> they have feedback but they accept with
[00:05:02] nits, you know. I I love that because
[00:05:04] you just everyone's just trusting each
[00:05:05] other, you know, move fast.
[00:05:06] >> Yeah.
[00:05:07] >> And I have some feedback, but
[00:05:09] >> it's not that important. It's just like
[00:05:12] >> take it if you will. Man, this is where
[00:05:13] I push that needle even further again.
[00:05:15] So, I will like even if I see your diff
[00:05:17] is going to blow up production.
[00:05:20] >> I will I will comment on it and be like,
[00:05:21] "This is going to blow up production."
[00:05:23] >> And then accept it and be like, "Yeah,
[00:05:25] make sure you fix that first." Right.
[00:05:27] And like I've never had a case where
[00:05:28] someone's like landed it.
[00:05:30] >> Yeah. like with a comment on it that
[00:05:32] says, "Hey, this is going to blow up
[00:05:33] production." Cuz you can can you imagine
[00:05:34] like sitting in SE review or something
[00:05:36] and someone's like,
[00:05:37] >> "The diff had a comment on it. This is
[00:05:39] going to blow up production." And it
[00:05:40] blow up.
[00:05:41] >> That's wild that.
[00:05:43] >> Yeah. Except I just trust him to fix it.
[00:05:45] Right. Like
[00:05:45] >> Yeah. Yeah. Yeah.
[00:05:46] >> Fix it the right way. Once again, if
[00:05:48] they have trust, if it's like a new
[00:05:49] person on the team and I'm not sure if
[00:05:51] they're going to fix it the right way,
[00:05:53] >> right, I might be like, "Ping me again
[00:05:54] when it's like ready."
[00:05:55] >> Yeah. Yeah.
[00:05:56] >> But yeah, 99% of the time, I'll just
[00:05:58] like accept and go.
[00:05:59] >> Yeah.
[00:05:59] >> And Yeah. haven't had to do the thing
[00:06:01] where I pull back because I've never had
[00:06:03] one that's been shipped accidentally
[00:06:05] >> exploded production.
[00:06:07] >> And that's actually a little bit of a
[00:06:08] philosophy I use across like I guess
[00:06:10] building these systems judging how fast
[00:06:12] I'm moving.
[00:06:14] >> If I'm doing something and it's not I'm
[00:06:16] not getting feedback that it's like
[00:06:17] broken or I'm not seeing negative
[00:06:19] effects from it, right? Even if it is
[00:06:21] controversial and crazy,
[00:06:22] >> I'll keep pushing the boundary on it,
[00:06:24] right? Same as our rollouts. Like if
[00:06:26] we're at 1% we're getting like very
[00:06:27] little feedback and like metrics are
[00:06:29] looking good and we might move to like
[00:06:32] 10% the next day and people are like
[00:06:33] that's crazy like step to like two three
[00:06:35] five things. It's like
[00:06:36] >> well not we're not getting any like
[00:06:38] >> signals that it's not going poorly.
[00:06:40] >> As soon as we get signals that it's
[00:06:42] going poorly we start pulling back. But
[00:06:44] >> otherwise I find you like move too
[00:06:46] slowly.
[00:06:46] >> Yeah.
[00:06:47] >> Right. You want to be moving at like the
[00:06:49] fastest speed you can without ruining
[00:06:51] things. Right. So, if you're not getting
[00:06:53] if you're not
[00:06:54] >> making anything worse, like keep trying
[00:06:56] to find that edge.
[00:06:57] >> Yeah. I I had a tech lead early in my
[00:07:00] career and I had taken down prod or
[00:07:02] something and I was talking to him about
[00:07:05] it and he you know at one on one end you
[00:07:08] shouldn't break prod generally but he
[00:07:11] also said if you never break prod
[00:07:15] that's probably not also optimal like
[00:07:17] there there should be some level of risk
[00:07:21] otherwise you're moving too slowly and
[00:07:23] so
[00:07:23] >> yeah exactly
[00:07:24] >> yeah try not to break prod But
[00:07:27] >> if you never break it, you're probably
[00:07:29] like very slow and
[00:07:30] >> Yeah. And if you're breaking it every
[00:07:32] day, you're probably going way too fast.
[00:07:34] Yeah.
[00:07:34] >> Exactly.
[00:07:36] >> Hey, thanks for watching that clip. If
[00:07:37] you thought it was interesting, it's
[00:07:39] part of a longer conversation which you
[00:07:40] can find right here, right now. And as
[00:07:43] always, if you have any feedback for me,
[00:07:44] I'd love to hear it. You can leave a
[00:07:46] comment on YouTube. I read every single
[00:07:48] one that I get.
