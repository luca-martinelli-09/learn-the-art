import os
import matplotlib.pyplot as plt
import numpy as np

class PlotUtils:
    titlePad = 30
    titleDim = 30
    xyLabelPad = 23
    xyLabelDim = 21
    xyTicksDim = 18
    gridAlpha = 0.2
    fillAlpha = 0.05
    barWidth = 0.95
    legendLoc = "upper left"
    legendLabelDim = 15
    colorScheme = ["#1DB954", "#22577A", "#A03C78", "#C67ACE"]
    figSize = (18, 8)
    figBGColor = None  # "w"
    figDPI = 500
    figBBox = "tight"
    figPad = .3
    figFormats = ["png", "pdf"]

    def __init__(self, options=None):
        self.setOptions(options)

    def setOptions(self, options):
        if options:
            self.titlePad = options["titlePad"] if "titlePad" in options.keys() else self.titlePad
            self.titleDim = options["titleDim"] if "titleDim" in options.keys() else self.titleDim
            self.xyLabelPad = options["xyLabelPad"] if "xyLabelPad" in options.keys() else self.xyLabelPad
            self.xyLabelDim = options["xyLabelDim"] if "xyLabelDim" in options.keys() else self.xyLabelDim
            self.xyTicksDim = options["xyTicksDim"] if "xyTicksDim" in options.keys() else self.xyTicksDim
            self.gridAlpha = options["gridAlpha"] if "gridAlpha" in options.keys() else self.gridAlpha
            self.fillAlpha = options["fillAlpha"] if "fillAlpha" in options.keys() else self.fillAlpha
            self.barWidth = options["barWidth"] if "barWidth" in options.keys() else self.barWidth
            self.legendLoc = options["legendLoc"] if "legendLoc" in options.keys() else self.legendLoc
            self.legendLabelDim = options["legendLabelDim"] if "legendLabelDim" in options.keys() else self.legendLabelDim
            self.colorScheme = options["colorScheme"] if "colorScheme" in options.keys() else self.colorScheme
            self.figSize = options["figSize"] if "figSize" in options.keys() else self.figSize
            self.figBGColor = options["figBGColor"] if "figBGColor" in options.keys() else self.figBGColor
            self.figDPI = options["figDPI"] if "figDPI" in options.keys() else self.figDPI
            self.figBBox = options["figBBox"] if "figBBox" in options.keys() else self.figBBox
            self.figPad = options["figPad"] if "figPad" in options.keys() else self.figPad
            self.figFormats = options["figFormats"] if "figFormats" in options.keys() else self.figFormats

    def _setLabelsAndTicks(self, xLabel=None, xTicks=None, xTicksPosition=None, xTicksRotation=0,
                        yLim=None, yLabel=None, yTicks=None, yTicksPosition=None, yTicksRotation=0):
        if not xLabel is None:
            plt.xlabel(xLabel, labelpad=self.xyLabelPad, fontsize=self.xyLabelDim)

        if not yLabel is None:
            plt.ylabel(yLabel, labelpad=self.xyLabelPad, fontsize=self.xyLabelDim)

        if not xTicks is None:
            if not xTicksPosition:
                xTicksPosition = self.x if self.style != "boxplot" else np.arange(0, self.numPlots)

                if self.style == "polar":
                    xTicks.append(xTicks[0])

            plt.xticks(xTicksPosition, xTicks, fontsize=self.xyTicksDim,
                    rotation=xTicksRotation)
        else:
            plt.xticks(fontsize=self.xyTicksDim, rotation=xTicksRotation)

        if not yTicks is None and not yTicksPosition is None:
            plt.yticks(yTicksPosition, yTicks, fontsize=self.xyTicksDim,
                    rotation=yTicksRotation)
        elif not yTicksPosition is None:
            plt.yticks(yTicksPosition, fontsize=self.xyTicksDim,
                    rotation=yTicksRotation)
        else:
            plt.yticks(fontsize=self.xyTicksDim, rotation=yTicksRotation)

        plt.ylim(top=yLim[1], bottom=yLim[0])


    def plotResults(self, title=None, x=[], yArr=[],
                    xLabel=None, xTicks=None, xTicksPosition=None, xTicksRotation=0,
                    yLim=None, yLabel=None, yTicks=None, yTicksPosition=None, yTicksRotation=0,
                    yErrors=None, legend=None,
                    style="line", showGrid=False, gridAxis="both", fillPlot=False,
                    twinIndexCut=None,
                    figSize=figSize, saveTitle=None):

        fig = plt.figure(figsize=figSize, facecolor=self.figBGColor)

        maxY = None
        minY = None

        numPlots = len(yArr)

        self.x = x
        self.yArr = yArr
        self.style = style
        self.numPlots = numPlots

        if twinIndexCut and numPlots < 2:
            raise ValueError(
                "With twinPlot=True you must have at least two data series")

        if twinIndexCut and style != "line" and style != "bar":
            raise ValueError("You can use twin plot only with line or bar")

        for i, y in zip(range(numPlots), self.yArr):
            label = None
            try:
                label = legend[i]
            except:
                pass

            yNum = [float(yVal) for yVal in y]
            maxY = np.max(
                [np.max(yNum), maxY]
            ) if not maxY is None else np.max(yNum)
            minY = np.min(
                [np.min(yNum), minY]
            ) if not minY is None else np.min(yNum)

            if style == "line" or style == "points":
                if yErrors:
                    plt.errorbar(self.x, yNum, yerr=yErrors[i], color=self.colorScheme[i],
                                 linestyle="", capsize=8, elinewidth=3, capthick=3)

                if style == "line":
                    plt.plot(self.x, yNum, label=label, color=self.colorScheme[i])
                else:
                    plt.plot(self.x, yNum, label=label, color=self.colorScheme[i], marker="o", linestyle="", markersize=8)

                if fillPlot:
                    plt.fill_between(self.x, yNum, alpha=self.fillAlpha,
                                     facecolor=self.colorScheme[i])

            elif style == "bar":
                barWidth = self.barWidth / numPlots
                xOffset = -self.barWidth / 2 + barWidth / 2 + barWidth * i
                plt.bar(self.x + xOffset, yNum, width=barWidth,
                        label=label, align="center", color=self.colorScheme[i])
                
                if yErrors:
                    plt.errorbar(self.x + xOffset, yNum, yerr=yErrors[i], color="#333333",
                                 linestyle="", capsize=8, elinewidth=2, capthick=2)

            elif style == "polar":
                self.x = np.linspace(
                    0, 2 * np.pi, len(yNum) + 1, endpoint=True)
                yNum.append(yNum[0])
                plt.polar(self.x, yNum, label=label, color=self.colorScheme[i])

                if fillPlot:
                    plt.fill(self.x, yNum, alpha=self.fillAlpha,
                            facecolor=self.colorScheme[i])

            elif style == "boxplot":
                lineWidth = 1.5

                if fillPlot:
                    plt.boxplot(yNum,
                                positions=[i],
                                notch=True,
                                widths=[1 / numPlots],
                                patch_artist=True,
                                showcaps=False,
                                showfliers=False,
                                showmeans=False,
                                boxprops=dict(
                                    facecolor=self.colorScheme[i],
                                    alpha=self.fillAlpha,
                                ),
                                )

                plt.boxplot(yNum,
                            positions=[i],
                            notch=True,
                            widths=[1 / numPlots],
                            boxprops=dict(
                                color=self.colorScheme[i],
                                linewidth=lineWidth,
                            ),
                            capprops=dict(
                                color=self.colorScheme[i],
                                linewidth=lineWidth,
                            ),
                            whiskerprops=dict(
                                color=self.colorScheme[i],
                                linewidth=lineWidth,
                            ),
                            flierprops=dict(
                                color=self.colorScheme[i],
                                markeredgecolor=self.colorScheme[i],
                                markerfacecolor=self.colorScheme[i],
                            ),
                            medianprops=dict(
                                color=self.colorScheme[i],
                                linewidth=lineWidth,
                            ),
                            )

            if not twinIndexCut is None and twinIndexCut == i:
                currYLim = yLim[0] if yLim else yLim
                currYLabel = yLabel[0] if yLabel else yLabel
                currYTicks = yTicks[0] if yTicks else yTicks
                currYTicksPosition = yTicksPosition[0] if yTicksPosition else yTicksPosition
                currYTicksRotation = yTicksRotation[0] if yTicksRotation else yTicksRotation

                if currYLim is None:
                    yPad = (maxY - minY) * 0.1
                    topLim = maxY + yPad * 2
                    infLim = minY - yPad if style == "bar" else minY - yPad
                    infLim = 0 if style == "bar" and minY >= 0 and minY <= yPad else infLim
                    infLim = minY if style == "polar" else infLim

                    currYLim = [infLim, topLim]

                self._setLabelsAndTicks(xLabel=xLabel, xTicks=xTicks, xTicksPosition=xTicksPosition, xTicksRotation=xTicksRotation,
                                yLim=currYLim, yLabel=currYLabel, yTicks=currYTicks, yTicksPosition=currYTicksPosition, yTicksRotation=currYTicksRotation)

                yLim = yLim[1] if yLim else yLim
                yLabel = yLabel[1] if yLabel else yLabel
                yTicks = yTicks[1] if yTicks else yTicks
                yTicksPosition = yTicksPosition[1] if yTicksPosition else yTicksPosition
                yTicksRotation = yTicksRotation[1] if yTicksRotation else yTicksRotation
                maxY = None
                minY = None

                plt.twinx()

        if yLim is None:
            yPad = (maxY - minY) * 0.1
            topLim = maxY + yPad * 2
            infLim = minY - yPad if style == "bar" else minY - yPad
            infLim = 0 if style == "bar" and minY >= 0 and minY <= yPad else infLim
            infLim = minY if style == "polar" else infLim

            yLim = [infLim, topLim]

        self._setLabelsAndTicks(xLabel=xLabel, xTicks=xTicks, xTicksPosition=xTicksPosition, xTicksRotation=xTicksRotation,
                        yLim=yLim, yLabel=yLabel, yTicks=yTicks, yTicksPosition=yTicksPosition, yTicksRotation=yTicksRotation)

        if showGrid:
            plt.grid(alpha=self.gridAlpha, axis=gridAxis)

        if not legend is None:
            if not twinIndexCut is None:
                fig.legend(loc=self.legendLoc, fontsize=self.legendLabelDim)
            else:
                plt.legend(loc=self.legendLoc, fontsize=self.legendLabelDim)
        
        if not title is None:
            plt.title(title, fontsize=self.titleDim, pad=self.titlePad)

        if not saveTitle is None:
            baseDir = "plots"
            if not os.path.exists(baseDir):
                os.mkdir("plots")

            for figFormat in self.figFormats:
                saveDir = baseDir + "/" + figFormat
                if not os.path.exists(saveDir):
                    os.mkdir(saveDir)

                plt.savefig(saveDir + "/" + saveTitle + "." + figFormat,
                            facecolor=self.figBGColor,
                            dpi=self.figDPI,
                            bbox_inches=self.figBBox,
                            pad_inches=self.figPad)

        plt.show()