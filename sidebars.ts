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
      label: 'Learning paradigms',
      items: ['learning/reinforcement-learning'],
    },
    {
      type: 'category',
      label: 'Knowledge systems',
      items: ['knowledge/rag'],
    },
    {
      type: 'category',
      label: 'Agents and skills',
      items: ['agents/agents-agentic-skills'],
    },
    {
      type: 'category',
      label: 'Autonomous systems',
      items: ['autonomy/autonomous-networks'],
    },
    {
      type: 'category',
      label: 'Living updates',
      items: ['updates/index'],
    },
  ],
};

export default sidebars;
