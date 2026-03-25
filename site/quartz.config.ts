import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Vault Corporativo",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "pt-BR",
    baseUrl: "totvs-vault.github.io/vault-corporativo",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      font: { header: "Inter", body: "Inter", code: "JetBrains Mono" },
      colors: {
        lightMode: {
          light: "#ffffff", lightgray: "#f2f2f2", gray: "#b3b3b3",
          darkgray: "#4a4a4a", dark: "#111111", secondary: "#1f4fd8",
          tertiary: "#6b7280", highlight: "rgba(31, 79, 216, 0.15)", textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618", lightgray: "#393639", gray: "#646464",
          darkgray: "#d4d4d4", dark: "#ebebec", secondary: "#7b97fa",
          tertiary: "#84a59d", highlight: "rgba(143, 159, 169, 0.15)", textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "filesystem"] }),
      Plugin.SyntaxHighlighting(),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(), Plugin.ComponentResources(), Plugin.ContentPage(),
      Plugin.FolderPage(), Plugin.TagPage(), Plugin.ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Plugin.Assets(), Plugin.Static(), Plugin.NotFoundPage(),
    ],
  },
}
export default config