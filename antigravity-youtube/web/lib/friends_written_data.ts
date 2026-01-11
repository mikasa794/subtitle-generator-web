import { PersonaType } from './friends_data';

export interface WrittenQuestion {
    id: string;
    scenario: { en: string; zh: string };
    options: {
        text: { en: string; zh: string };
        persona: PersonaType;
        feedback: { en: string; zh: string };
    }[];
}

export const FRIENDS_WRITTEN_DATA: WrittenQuestion[] = [
    {
        id: 'w1',
        scenario: {
            en: "Someone at work ate your sandwich. It was the only good thing going on in your life.",
            zh: "同事偷吃了你的三明治（那可是包含独家配方Moist Maker的完美三明治）。那是你悲惨生活中唯一的慰藉。"
        },
        options: [
            {
                text: { en: "Yell at them. Scream 'MY SANDWICH?!' until the birds fly away.", zh: "对他咆哮：'MY SANDWICH?!' 吼到把鸽子都吓飞。" },
                persona: 'Ross',
                feedback: { en: "You have some rage issues, Geller.", zh: "你的怒气值有点高啊，Geller博士。" }
            },
            {
                text: { en: "Write a passive-aggressive note to scare them off.", zh: "写一张充满威胁语气的便条贴在冰箱上。" },
                persona: 'Ross',
                feedback: { en: "Ah, the 'Mental Geller' approach.", zh: "这就是传说中的 'Mental Geller' 战术。" }
            },
            {
                text: { en: "Avoid confrontation. Make a joke about it to your friends later.", zh: "避免正面冲突，回去跟朋友吐槽并在背后讲笑话。" },
                persona: 'Chandler',
                feedback: { en: "Could you BE any more non-confrontational?", zh: "你还能再怂一点吗？" }
            },
            {
                text: { en: "Make them a new sandwich. Maybe they were just hungry?", zh: "给他做一个新的。也许他只是太饿了？" },
                persona: 'Phoebe',
                feedback: { en: "You're too pure for this world, Phoebe.", zh: "你在这个残酷的世界里太纯真了，Phoebe。" }
            }
        ]
    },
    {
        id: 'w2',
        scenario: {
            en: "You and your partner just had a huge fight and 'took a break'. You meet someone cute at a bar the same night. What do you do?",
            zh: "你和对象刚大吵一架并决定 'Take a break'。当晚你在酒吧遇到了一个辣妹/帅哥。你会："
        },
        options: [
            {
                text: { en: "Hook up with them. We are ON A BREAK!", zh: "睡了再说！我们要分手了（We are ON A BREAK）！" },
                persona: 'Ross',
                feedback: { en: "Technicalities won't save you from Rachel's wrath.", zh: "但在技术层面你确实没错...可是Rachel会杀了你的。" }
            },
            {
                text: { en: "Call your friends to analyze the situation for 3 hours.", zh: "立刻召集朋友开会分析局势，并在白板上画出利弊图。" },
                persona: 'Monica',
                feedback: { en: "You need a plan and a whiteboard.", zh: "你需要一个计划，还有一块白板。" }
            },
            {
                text: { en: "Go home and eat a tub of ice cream.", zh: "回家，吃掉一整桶冰淇淋。" },
                persona: 'Rachel',
                feedback: { en: "Classic coping mechanism.", zh: "经典的瑞秋式疗伤法。" }
            },
            {
                text: { en: "Flirt with them, but don't do anything serious. 'How you doin'?'", zh: "调个情，但不来真的。'How you doin'?'" },
                persona: 'Joey',
                feedback: { en: "Always testing the waters.", zh: "永远在试水温的 Joey。" }
            }
        ]
    },
    {
        id: 'w3',
        scenario: {
            en: "Your friend has a terrible secret (like they're secretly dating your other friend). You find out. usage?",
            zh: "你发现朋友藏着一个惊天大秘密（比如她在偷偷跟另一个朋友约会）。你会："
        },
        options: [
            {
                text: { en: "Keep it. Secrets are your vault.", zh: "死守秘密。你就是保险箱。" },
                persona: 'Ross',
                feedback: { en: "Surprisingly, you might be the best secret keeper (like Joey).", zh: "没想到吧，你其实很能藏事（像Joey一样）。" }
            },
            {
                text: { en: "Crack under pressure and shout it out at a quiet moment.", zh: "压力太大绷不住了，在大家安静的时候突然喊出来。" },
                persona: 'Chandler',
                feedback: { en: "Chandler can't handle the pressure!", zh: "Chandler 根本抗压能力为零！" }
            },
            {
                text: { en: "Use the secret to mess with them for fun. 'They don't know that we know they know!'", zh: "利用这个秘密跟他们玩心理战。'They don't know that we know they know!'" },
                persona: 'Phoebe',
                feedback: { en: "Regina Phalange loves the chaos.", zh: "Regina Phalange 最喜欢混乱了。" }
            },
            {
                text: { en: "Gossip immediately. Everyone needs to know.", zh: "立刻八卦出去。这种大事怎么能只有我知道！" },
                persona: 'Rachel',
                feedback: { en: "You just can't help yourself.", zh: "你就是管不住这唯一的一张嘴。" }
            }
        ]
    },
    {
        id: 'w4',
        scenario: {
            en: "You're planning a surprise party for a friend.",
            zh: "你正在给朋友策划一个惊喜派对。"
        },
        options: [
            {
                text: { en: "Create a strictly timed schedule. 8:00 - Surprise. 8:05 - Cake.", zh: "制定严格的时间表。8:00 - 惊喜。8:05 - 切蛋糕。" },
                persona: 'Monica',
                feedback: { en: "Fun is only fun if it's scheduled.", zh: "只有按计划进行的快乐才是真正的快乐。" }
            },
            {
                text: { en: "Forget to invite half the people.", zh: "这那的...结果忘了邀请一半的人。" },
                persona: 'Rachel',
                feedback: { en: "You tried your best.", zh: "你...尽力了。" }
            },
            {
                text: { en: "Bring cups. And ice. Costs split 3 ways.", zh: "带杯子。还有冰块。费用我要跟大家AA。" },
                persona: 'Chandler',
                feedback: { en: "You're just here for the cups.", zh: "你就是那个负责买杯子的工具人。" }
            },
            {
                text: { en: "Bring a guitar and sing a song about their mortality.", zh: "带吉他，为寿星献唱一首关于'死亡与轮回'的歌。" },
                persona: 'Phoebe',
                feedback: { en: "Smelly Cat, Smelly Cat...", zh: "臭臭猫，臭臭猫..." }
            }
        ]
    }
];
