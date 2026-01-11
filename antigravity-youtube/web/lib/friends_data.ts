export type PersonaType = 'Joey' | 'Monica' | 'Ross' | 'Phoebe' | 'Rachel' | 'Chandler';

export interface QuizQuestion {
    id: string;
    videoId: string;
    clipStart: number;
    clipEnd: number;
    question: string;
    subs?: { en: string; zh: string };
    options: {
        text: string;
        persona: PersonaType;
        feedback: string;
    }[];
}

export const FRIENDS_QUIZ_DATA: QuizQuestion[] = [
    {
        id: 'q1',
        videoId: 'zQUO39j_c_k', // Joey doesn't share food
        clipStart: 0,
        clipEnd: 38,
        question: "Your date steals a few fries from your plate. You...",
        subs: {
            en: "JOEY DOESN'T SHARE FOOD!",
            zh: "Joey 从不分享食物！"
        },
        options: [
            {
                text: "Scream 'JOEY DOESN'T SHARE FOOD!' and protect your plate.",
                persona: 'Joey',
                feedback: "Food is sacred. We get it."
            },
            {
                text: "Say nothing, but silently judge their lack of manners.",
                persona: 'Monica',
                feedback: "The internal rage is real."
            },
            {
                text: "Let them have it, I'm probably on a diet anyway.",
                persona: 'Rachel',
                feedback: "Rachel Green vibes."
            }
        ]
    },
    {
        id: 'q2',
        videoId: 'L_PWbnHABsM', // PIVOT
        clipStart: 10,
        clipEnd: 40,
        question: "You're helping a friend move a couch and it's stuck. You...",
        subs: {
            en: "PIVOT! PIVOT! PIVOT!",
            zh: "转弯！转弯！转弯！"
        },
        options: [
            {
                text: "Draw a diagram to calculate the optimal angle.",
                persona: 'Ross',
                feedback: "Science is the answer to everything."
            },
            {
                text: "Make a sarcastic joke about how heavy it is.",
                persona: 'Chandler',
                feedback: "Humor is your defense mechanism."
            },
            {
                text: "Yell instructions louder until it fits.",
                persona: 'Monica',
                feedback: "You're definitely in charge here."
            }
        ]
    },
    {
        id: 'q3',
        videoId: 'UPW3iSLPrPg', // Unagi
        clipStart: 10,
        clipEnd: 50,
        question: "You're walking home alone at night. You rely on...",
        subs: {
            en: "Unagi is a state of total awareness.",
            zh: "Unagi 是一种完全觉知的状态。"
        },
        options: [
            {
                text: "Unagi (Total Awareness). I am prepared for anything.",
                persona: 'Ross',
                feedback: "Watch out for jump scares though!"
            },
            {
                text: "My street smarts (and maybe a little screaming).",
                persona: 'Phoebe',
                feedback: "Street Phoebe is not to be messed with."
            },
            {
                text: "Running away very fast.",
                persona: 'Chandler',
                feedback: "Flight > Fight."
            }
        ]
    },
    {
        id: 'q4',
        videoId: 'lkbr5qnYSUU', // Bill Split
        clipStart: 60,
        clipEnd: 100,
        question: "Group dinner is over. The bill arrives. You...",
        subs: {
            en: "We'll split it five ways, that's only...",
            zh: "我们五个人平分，每人只要..."
        },
        options: [
            {
                text: "Calculate exactly what everyone owes down to the cent.",
                persona: 'Monica',
                feedback: "Fair is fair (and organized)!"
            },
            {
                text: "Pay only for my side salad.",
                persona: 'Phoebe',
                feedback: "Principles matter."
            },
            {
                text: "Hope someone else pays because I'm broke.",
                persona: 'Joey',
                feedback: "How you doin' on cash?"
            }
        ]
    },
    {
        id: 'q5',
        videoId: 'JYqAWNVHBwo', // My Eyes! My Eyes!
        clipStart: 6,
        clipEnd: 25,
        question: "You accidentally see your best friends hooking up. You...",
        subs: {
            en: "MY EYES! MY EYES!",
            zh: "我的眼睛！我的眼睛！"
        },
        options: [
            {
                text: "Scream 'MY EYES! MY EYES!'",
                persona: 'Phoebe',
                feedback: "Traumatized for life."
            },
            {
                text: "Stand there in shock and try to process the logic.",
                persona: 'Ross',
                feedback: "It DOES make sense if you think about it."
            },
            {
                text: "Gossip about it immediately with everyone else.",
                persona: 'Rachel',
                feedback: "You love the drama."
            }
        ]
    }
];
