Week 3

**What is the AI agent?**
An AI agent is any system that:
<br/> - Perceives its environment (via sensors or input)
<br/> - Decides what action to take
<br/> - Acts on the environment to achieve a goal

Agent = Sensor + Brain (policy/decision-making) + Actuator

It could be:
<br/> - A robot moving around a room
<br/> - A chatbot giving you recommendations
<br/> - An autonomous car deciding to stop at a red light
<br/> - An LLM using tools (search, calculator, etc.)

**What is the connection between AI agents and Reinforcement Learning?**
<br/>Reinforcement Learning is how an AI agent can learn to become *intelligent*.
<br/>Reinforcement Learning is a training method for agents. It teaches an agent how to act based on trial and error and rewards.

**LLM-based AI Agents + RL**
<br/>In modern AI agents (like GPT), RL is often used to:
<br/> - Fine-tune responses based on human feedback (RLHF)
<br/> - Train tool-using behavior (e.g., LLM learns when to call a search function)
<br/> - Explore and optimize policies (e.g., what sequence of actions solves a task)

**Multi-Agent Reinforcement Learning (MARL)**
<br/>MARL is when multiple agents learn and act in a shared environment. Instead of a single agent learning to maximize its reward, you now have two or more agents:
<br/> - Cooperating
<br/> - Competing
<br/> - a mix of both

**Reinforcement Learning from Human Feedback (RLHF)**
<br/>RLHF is a way to train AI systems—especially language models—by using human feedback as the reward signal, instead of hardcoded numbers. It's a safer and more aligned approach when:
<br/> - Defining a numerical reward is too hard (e.g., "How helpful was this answer?")
<br/> - You want models that behave in human-preferred ways

**How it works with LLMs**
<br/> - Pretrain LLM using massive text data (unsupervised)
<br/> - Collect human feedback: Show multiple outputs to annotators, who rank them (e.g., "Answer A is better than B")
<br/> - Train a reward model to mimic human preferences
<br/> - Fine-tune the LLM using RL to maximize the learned reward

Reference:
<br/>https://www.datacamp.com/blog/ai-agents
<br/>https://www.anthropic.com/engineering/building-effective-agents
<br/>https://aws.amazon.com/what-is/ai-agents/
<br/>https://techcommunity.microsoft.com/blog/educatordeveloperblog/building-ai-agent-applications-series---understanding-ai-agents/4046944
<br/>https://en.wikipedia.org/wiki/Multi-agent_reinforcement_learning
<br/>https://adasci.org/all-you-need-to-know-about-multi-agent-reinforcement-learning/
<br/>https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback
<br/>https://aws.amazon.com/what-is/reinforcement-learning-from-human-feedback/