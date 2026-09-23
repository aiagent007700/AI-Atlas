import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'The AI atlas',
      items: ['atlas/roadmap'],
    },
    {
      type: 'category',
      label: 'Foundations',
      items: ['foundations/ai-foundations'],
    },
    {
      type: 'category',
      label: 'Evaluation',
      items: ['evaluation/ai-system-evaluation'],
    },
    {
      type: 'category',
      label: 'Learning paradigms',
      items: ['learning/reinforcement-learning'],
    },
    {
      type: 'category',
      label: 'Knowledge systems',
      items: ['knowledge/rag', 'knowledge/rag-evaluation'],
    },
    {
      type: 'category',
      label: 'Agents and skills',
      items: ['agents/agents-agentic-skills', 'agents/skill-anatomy'],
    },
    {
      type: 'category',
      label: 'Evidence and industry',
      items: ['evidence/industry-voices'],
    },
    {
      type: 'category',
      label: 'Autonomous systems',
      items: ['autonomy/autonomous-networks'],
    },
    {
      type: 'category',
      label: 'Visual grammar',
      items: ['visuals/visual-language'],
    },
    {
      type: 'category',
      label: 'Living updates',
      items: ['updates/index', 'updates/template'],
    },
  ],
};

export default sidebars;
