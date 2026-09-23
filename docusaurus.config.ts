import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const repository = process.env.GITHUB_REPOSITORY ?? '';
const [repositoryOwner = 'YOUR_GITHUB_USER', repositoryName = 'ai-living-tutorial'] = repository.split('/');
const isUserSite = repositoryName === `${repositoryOwner}.github.io`;

const config: Config = {
  title: 'AI Atlas',
  tagline: 'A living tutorial across the breadth of artificial intelligence',
  favicon: 'img/ai-atlas-loop.svg',
  url: process.env.DOCUSAURUS_URL ?? `https://${repositoryOwner}.github.io`,
  baseUrl: process.env.DOCUSAURUS_BASE_URL ?? (isUserSite ? '/' : `/${repositoryName}/`),
  organizationName: repositoryOwner,
  projectName: repositoryName,
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  trailingSlash: false,
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          showLastUpdateTime: true,
          editUrl: `https://github.com/${repositoryOwner}/${repositoryName}/tree/main/`,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],
  themes: ['@docusaurus/theme-mermaid'],
  markdown: {
    mermaid: true,
  },
  themeConfig: {
    image: 'img/ai-atlas-loop.svg',
    navbar: {
      title: 'AI Atlas',
      logo: {
        alt: 'AI Atlas loop',
        src: 'img/ai-atlas-loop.svg',
      },
      items: [
        {to: '/docs/intro', label: 'Start here', position: 'left'},
        {to: '/docs/atlas/roadmap', label: 'Atlas', position: 'left'},
        {to: '/docs/updates', label: 'Daily updates', position: 'left'},
        {
          href: `https://github.com/${repositoryOwner}/${repositoryName}`,
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Explore',
          items: [
            {label: 'Start here', to: '/docs/intro'},
            {label: 'AI atlas', to: '/docs/atlas/roadmap'},
            {label: 'Daily updates', to: '/docs/updates'},
          ],
        },
        {
          title: 'Principles',
          items: [
            {label: 'Evidence first', to: '/docs/intro#evidence-first'},
            {label: 'Thought experiments', to: '/docs/intro#thought-provoking-by-design'},
          ],
        },
      ],
      copyright: `AI Atlas • ${new Date().getFullYear()}`,
    },
    prism: {
      theme: {
        plain: {color: '#24324a', backgroundColor: '#f5f8fc'},
        styles: [],
      },
      darkTheme: {
        plain: {color: '#e6edf7', backgroundColor: '#111827'},
        styles: [],
      },
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
