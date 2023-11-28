# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
foamfoam = OpenFOAMReader(registrationName='foam.foam', FileName='D:\\Skole\\Uni\\ExternalFlow\\simulation\\10\\simulation\\foam.foam')
foamfoam.SkipZeroTime = 1
foamfoam.CaseType = 'Reconstructed Case'
foamfoam.LabelSize = '32-bit'
foamfoam.ScalarSize = '64-bit (DP)'
foamfoam.Createcelltopointfiltereddata = 1
foamfoam.Adddimensionalunitstoarraynames = 0
foamfoam.MeshRegions = ['internalMesh']
foamfoam.CellArrays = ['U', 'nuTilda', 'nut', 'p']
foamfoam.PointArrays = []
foamfoam.LagrangianArrays = []
foamfoam.Cachemesh = 1
foamfoam.Decomposepolyhedra = 1
foamfoam.ListtimestepsaccordingtocontrolDict = 0
foamfoam.Lagrangianpositionswithoutextradata = 1
foamfoam.Readzones = 0
foamfoam.Copydatatocellzones = 0

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# Properties modified on renderView1
renderView1.CameraParallelProjection = 1

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Properties modified on foamfoam
foamfoam.Decomposepolyhedra = 0

# show data in view
foamfoamDisplay = Show(foamfoam, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')
pTF2D.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
pTF2D.Boxes = []
pTF2D.ScalarRangeInitialized = 0
pTF2D.Range = [0.0, 1.0, 0.0, 1.0]
pTF2D.OutputDimensions = [10, 10]

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
pLUT.InterpretValuesAsCategories = 0
pLUT.AnnotationsInitialized = 0
pLUT.ShowCategoricalColorsinDataRangeOnly = 0
pLUT.RescaleOnVisibilityChange = 0
pLUT.EnableOpacityMapping = 0
pLUT.TransferFunction2D = pTF2D
pLUT.Use2DTransferFunction = 0
pLUT.RGBPoints = [-0.8886154890060425, 0.231373, 0.298039, 0.752941, -0.19472377002239227, 0.865003, 0.865003, 0.865003, 0.49916794896125793, 0.705882, 0.0156863, 0.14902]
pLUT.UseLogScale = 0
pLUT.UseOpacityControlPointsFreehandDrawing = 0
pLUT.ShowDataHistogram = 0
pLUT.AutomaticDataHistogramComputation = 0
pLUT.DataHistogramNumberOfBins = 10
pLUT.ColorSpace = 'Diverging'
pLUT.UseBelowRangeColor = 0
pLUT.BelowRangeColor = [0.0, 0.0, 0.0]
pLUT.UseAboveRangeColor = 0
pLUT.AboveRangeColor = [0.5, 0.5, 0.5]
pLUT.NanColor = [1.0, 1.0, 0.0]
pLUT.NanOpacity = 1.0
pLUT.Discretize = 1
pLUT.NumberOfTableValues = 256
pLUT.ScalarRangeInitialized = 1.0
pLUT.HSVWrap = 0
pLUT.VectorComponent = 0
pLUT.VectorMode = 'Magnitude'
pLUT.AllowDuplicateScalars = 1
pLUT.Annotations = []
pLUT.ActiveAnnotatedValues = []
pLUT.IndexedColors = []
pLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Points = [-0.8886154890060425, 0.0, 0.5, 0.0, 0.49916794896125793, 1.0, 0.5, 0.0]
pPWF.AllowDuplicateScalars = 1
pPWF.UseLogScale = 0
pPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
foamfoamDisplay.Selection = None
foamfoamDisplay.Representation = 'Surface'
foamfoamDisplay.ColorArrayName = ['POINTS', 'p']
foamfoamDisplay.LookupTable = pLUT
foamfoamDisplay.MapScalars = 1
foamfoamDisplay.MultiComponentsMapping = 0
foamfoamDisplay.InterpolateScalarsBeforeMapping = 1
foamfoamDisplay.Opacity = 1.0
foamfoamDisplay.PointSize = 2.0
foamfoamDisplay.LineWidth = 1.0
foamfoamDisplay.RenderLinesAsTubes = 0
foamfoamDisplay.RenderPointsAsSpheres = 0
foamfoamDisplay.Interpolation = 'Gouraud'
foamfoamDisplay.Specular = 0.0
foamfoamDisplay.SpecularColor = [1.0, 1.0, 1.0]
foamfoamDisplay.SpecularPower = 100.0
foamfoamDisplay.Luminosity = 0.0
foamfoamDisplay.Ambient = 0.0
foamfoamDisplay.Diffuse = 1.0
foamfoamDisplay.Roughness = 0.3
foamfoamDisplay.Metallic = 0.0
foamfoamDisplay.EdgeTint = [1.0, 1.0, 1.0]
foamfoamDisplay.Anisotropy = 0.0
foamfoamDisplay.AnisotropyRotation = 0.0
foamfoamDisplay.BaseIOR = 1.5
foamfoamDisplay.CoatStrength = 0.0
foamfoamDisplay.CoatIOR = 2.0
foamfoamDisplay.CoatRoughness = 0.0
foamfoamDisplay.CoatColor = [1.0, 1.0, 1.0]
foamfoamDisplay.SelectTCoordArray = 'None'
foamfoamDisplay.SelectNormalArray = 'None'
foamfoamDisplay.SelectTangentArray = 'None'
foamfoamDisplay.Texture = None
foamfoamDisplay.RepeatTextures = 1
foamfoamDisplay.InterpolateTextures = 0
foamfoamDisplay.SeamlessU = 0
foamfoamDisplay.SeamlessV = 0
foamfoamDisplay.UseMipmapTextures = 0
foamfoamDisplay.ShowTexturesOnBackface = 1
foamfoamDisplay.BaseColorTexture = None
foamfoamDisplay.NormalTexture = None
foamfoamDisplay.NormalScale = 1.0
foamfoamDisplay.CoatNormalTexture = None
foamfoamDisplay.CoatNormalScale = 1.0
foamfoamDisplay.MaterialTexture = None
foamfoamDisplay.OcclusionStrength = 1.0
foamfoamDisplay.AnisotropyTexture = None
foamfoamDisplay.EmissiveTexture = None
foamfoamDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
foamfoamDisplay.FlipTextures = 0
foamfoamDisplay.BackfaceRepresentation = 'Follow Frontface'
foamfoamDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
foamfoamDisplay.BackfaceOpacity = 1.0
foamfoamDisplay.Position = [0.0, 0.0, 0.0]
foamfoamDisplay.Scale = [1.0, 1.0, 1.0]
foamfoamDisplay.Orientation = [0.0, 0.0, 0.0]
foamfoamDisplay.Origin = [0.0, 0.0, 0.0]
foamfoamDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
foamfoamDisplay.Pickable = 1
foamfoamDisplay.Triangulate = 0
foamfoamDisplay.UseShaderReplacements = 0
foamfoamDisplay.ShaderReplacements = ''
foamfoamDisplay.NonlinearSubdivisionLevel = 1
foamfoamDisplay.UseDataPartitions = 0
foamfoamDisplay.OSPRayUseScaleArray = 'All Approximate'
foamfoamDisplay.OSPRayScaleArray = 'p'
foamfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
foamfoamDisplay.OSPRayMaterial = 'None'
foamfoamDisplay.BlockSelectors = ['/']
foamfoamDisplay.BlockColors = []
foamfoamDisplay.BlockOpacities = []
foamfoamDisplay.Orient = 0
foamfoamDisplay.OrientationMode = 'Direction'
foamfoamDisplay.SelectOrientationVectors = 'U'
foamfoamDisplay.Scaling = 0
foamfoamDisplay.ScaleMode = 'No Data Scaling Off'
foamfoamDisplay.ScaleFactor = 4.0
foamfoamDisplay.SelectScaleArray = 'p'
foamfoamDisplay.GlyphType = 'Arrow'
foamfoamDisplay.UseGlyphTable = 0
foamfoamDisplay.GlyphTableIndexArray = 'p'
foamfoamDisplay.UseCompositeGlyphTable = 0
foamfoamDisplay.UseGlyphCullingAndLOD = 0
foamfoamDisplay.LODValues = []
foamfoamDisplay.ColorByLODIndex = 0
foamfoamDisplay.GaussianRadius = 0.2
foamfoamDisplay.ShaderPreset = 'Sphere'
foamfoamDisplay.CustomTriangleScale = 3
foamfoamDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
foamfoamDisplay.Emissive = 0
foamfoamDisplay.ScaleByArray = 0
foamfoamDisplay.SetScaleArray = ['POINTS', 'p']
foamfoamDisplay.ScaleArrayComponent = ''
foamfoamDisplay.UseScaleFunction = 1
foamfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
foamfoamDisplay.OpacityByArray = 0
foamfoamDisplay.OpacityArray = ['POINTS', 'p']
foamfoamDisplay.OpacityArrayComponent = ''
foamfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
foamfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
foamfoamDisplay.SelectionCellLabelBold = 0
foamfoamDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
foamfoamDisplay.SelectionCellLabelFontFamily = 'Arial'
foamfoamDisplay.SelectionCellLabelFontFile = ''
foamfoamDisplay.SelectionCellLabelFontSize = 18
foamfoamDisplay.SelectionCellLabelItalic = 0
foamfoamDisplay.SelectionCellLabelJustification = 'Left'
foamfoamDisplay.SelectionCellLabelOpacity = 1.0
foamfoamDisplay.SelectionCellLabelShadow = 0
foamfoamDisplay.SelectionPointLabelBold = 0
foamfoamDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
foamfoamDisplay.SelectionPointLabelFontFamily = 'Arial'
foamfoamDisplay.SelectionPointLabelFontFile = ''
foamfoamDisplay.SelectionPointLabelFontSize = 18
foamfoamDisplay.SelectionPointLabelItalic = 0
foamfoamDisplay.SelectionPointLabelJustification = 'Left'
foamfoamDisplay.SelectionPointLabelOpacity = 1.0
foamfoamDisplay.SelectionPointLabelShadow = 0
foamfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
foamfoamDisplay.ScalarOpacityFunction = pPWF
foamfoamDisplay.ScalarOpacityUnitDistance = 1.2341798864881979
foamfoamDisplay.UseSeparateOpacityArray = 0
foamfoamDisplay.OpacityArrayName = ['POINTS', 'p']
foamfoamDisplay.OpacityComponent = ''
foamfoamDisplay.SelectMapper = 'Projected tetra'
foamfoamDisplay.SamplingDimensions = [128, 128, 128]
foamfoamDisplay.UseFloatingPointFrameBuffer = 1
foamfoamDisplay.SelectInputVectors = ['POINTS', 'U']
foamfoamDisplay.NumberOfSteps = 40
foamfoamDisplay.StepSize = 0.25
foamfoamDisplay.NormalizeVectors = 1
foamfoamDisplay.EnhancedLIC = 1
foamfoamDisplay.ColorMode = 'Blend'
foamfoamDisplay.LICIntensity = 0.8
foamfoamDisplay.MapModeBias = 0.0
foamfoamDisplay.EnhanceContrast = 'Off'
foamfoamDisplay.LowLICContrastEnhancementFactor = 0.0
foamfoamDisplay.HighLICContrastEnhancementFactor = 0.0
foamfoamDisplay.LowColorContrastEnhancementFactor = 0.0
foamfoamDisplay.HighColorContrastEnhancementFactor = 0.0
foamfoamDisplay.AntiAlias = 0
foamfoamDisplay.MaskOnSurface = 1
foamfoamDisplay.MaskThreshold = 0.0
foamfoamDisplay.MaskIntensity = 0.0
foamfoamDisplay.MaskColor = [0.5, 0.5, 0.5]
foamfoamDisplay.GenerateNoiseTexture = 0
foamfoamDisplay.NoiseType = 'Gaussian'
foamfoamDisplay.NoiseTextureSize = 128
foamfoamDisplay.NoiseGrainSize = 2
foamfoamDisplay.MinNoiseValue = 0.0
foamfoamDisplay.MaxNoiseValue = 0.8
foamfoamDisplay.NumberOfNoiseLevels = 1024
foamfoamDisplay.ImpulseNoiseProbability = 1.0
foamfoamDisplay.ImpulseNoiseBackgroundValue = 0.0
foamfoamDisplay.NoiseGeneratorSeed = 1
foamfoamDisplay.CompositeStrategy = 'AUTO'
foamfoamDisplay.UseLICForLOD = 0
foamfoamDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
foamfoamDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
foamfoamDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
foamfoamDisplay.GlyphType.TipResolution = 6
foamfoamDisplay.GlyphType.TipRadius = 0.1
foamfoamDisplay.GlyphType.TipLength = 0.35
foamfoamDisplay.GlyphType.ShaftResolution = 6
foamfoamDisplay.GlyphType.ShaftRadius = 0.03
foamfoamDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
foamfoamDisplay.ScaleTransferFunction.Points = [-0.8886154890060425, 0.0, 0.5, 0.0, 0.49916794896125793, 1.0, 0.5, 0.0]
foamfoamDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
foamfoamDisplay.OpacityTransferFunction.Points = [-0.8886154890060425, 0.0, 0.5, 0.0, 0.49916794896125793, 1.0, 0.5, 0.0]
foamfoamDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
foamfoamDisplay.DataAxesGrid.XTitle = 'X Axis'
foamfoamDisplay.DataAxesGrid.YTitle = 'Y Axis'
foamfoamDisplay.DataAxesGrid.ZTitle = 'Z Axis'
foamfoamDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
foamfoamDisplay.DataAxesGrid.XTitleFontFile = ''
foamfoamDisplay.DataAxesGrid.XTitleBold = 0
foamfoamDisplay.DataAxesGrid.XTitleItalic = 0
foamfoamDisplay.DataAxesGrid.XTitleFontSize = 12
foamfoamDisplay.DataAxesGrid.XTitleShadow = 0
foamfoamDisplay.DataAxesGrid.XTitleOpacity = 1.0
foamfoamDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
foamfoamDisplay.DataAxesGrid.YTitleFontFile = ''
foamfoamDisplay.DataAxesGrid.YTitleBold = 0
foamfoamDisplay.DataAxesGrid.YTitleItalic = 0
foamfoamDisplay.DataAxesGrid.YTitleFontSize = 12
foamfoamDisplay.DataAxesGrid.YTitleShadow = 0
foamfoamDisplay.DataAxesGrid.YTitleOpacity = 1.0
foamfoamDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
foamfoamDisplay.DataAxesGrid.ZTitleFontFile = ''
foamfoamDisplay.DataAxesGrid.ZTitleBold = 0
foamfoamDisplay.DataAxesGrid.ZTitleItalic = 0
foamfoamDisplay.DataAxesGrid.ZTitleFontSize = 12
foamfoamDisplay.DataAxesGrid.ZTitleShadow = 0
foamfoamDisplay.DataAxesGrid.ZTitleOpacity = 1.0
foamfoamDisplay.DataAxesGrid.FacesToRender = 63
foamfoamDisplay.DataAxesGrid.CullBackface = 0
foamfoamDisplay.DataAxesGrid.CullFrontface = 1
foamfoamDisplay.DataAxesGrid.ShowGrid = 0
foamfoamDisplay.DataAxesGrid.ShowEdges = 1
foamfoamDisplay.DataAxesGrid.ShowTicks = 1
foamfoamDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
foamfoamDisplay.DataAxesGrid.AxesToLabel = 63
foamfoamDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
foamfoamDisplay.DataAxesGrid.XLabelFontFile = ''
foamfoamDisplay.DataAxesGrid.XLabelBold = 0
foamfoamDisplay.DataAxesGrid.XLabelItalic = 0
foamfoamDisplay.DataAxesGrid.XLabelFontSize = 12
foamfoamDisplay.DataAxesGrid.XLabelShadow = 0
foamfoamDisplay.DataAxesGrid.XLabelOpacity = 1.0
foamfoamDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
foamfoamDisplay.DataAxesGrid.YLabelFontFile = ''
foamfoamDisplay.DataAxesGrid.YLabelBold = 0
foamfoamDisplay.DataAxesGrid.YLabelItalic = 0
foamfoamDisplay.DataAxesGrid.YLabelFontSize = 12
foamfoamDisplay.DataAxesGrid.YLabelShadow = 0
foamfoamDisplay.DataAxesGrid.YLabelOpacity = 1.0
foamfoamDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
foamfoamDisplay.DataAxesGrid.ZLabelFontFile = ''
foamfoamDisplay.DataAxesGrid.ZLabelBold = 0
foamfoamDisplay.DataAxesGrid.ZLabelItalic = 0
foamfoamDisplay.DataAxesGrid.ZLabelFontSize = 12
foamfoamDisplay.DataAxesGrid.ZLabelShadow = 0
foamfoamDisplay.DataAxesGrid.ZLabelOpacity = 1.0
foamfoamDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
foamfoamDisplay.DataAxesGrid.XAxisPrecision = 2
foamfoamDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
foamfoamDisplay.DataAxesGrid.XAxisLabels = []
foamfoamDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
foamfoamDisplay.DataAxesGrid.YAxisPrecision = 2
foamfoamDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
foamfoamDisplay.DataAxesGrid.YAxisLabels = []
foamfoamDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
foamfoamDisplay.DataAxesGrid.ZAxisPrecision = 2
foamfoamDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
foamfoamDisplay.DataAxesGrid.ZAxisLabels = []
foamfoamDisplay.DataAxesGrid.UseCustomBounds = 0
foamfoamDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
foamfoamDisplay.PolarAxes.Visibility = 0
foamfoamDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
foamfoamDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
foamfoamDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
foamfoamDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
foamfoamDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
foamfoamDisplay.PolarAxes.EnableCustomRange = 0
foamfoamDisplay.PolarAxes.CustomRange = [0.0, 1.0]
foamfoamDisplay.PolarAxes.PolarAxisVisibility = 1
foamfoamDisplay.PolarAxes.RadialAxesVisibility = 1
foamfoamDisplay.PolarAxes.DrawRadialGridlines = 1
foamfoamDisplay.PolarAxes.PolarArcsVisibility = 1
foamfoamDisplay.PolarAxes.DrawPolarArcsGridlines = 1
foamfoamDisplay.PolarAxes.NumberOfRadialAxes = 0
foamfoamDisplay.PolarAxes.AutoSubdividePolarAxis = 1
foamfoamDisplay.PolarAxes.NumberOfPolarAxis = 0
foamfoamDisplay.PolarAxes.MinimumRadius = 0.0
foamfoamDisplay.PolarAxes.MinimumAngle = 0.0
foamfoamDisplay.PolarAxes.MaximumAngle = 90.0
foamfoamDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
foamfoamDisplay.PolarAxes.Ratio = 1.0
foamfoamDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
foamfoamDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
foamfoamDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
foamfoamDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
foamfoamDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
foamfoamDisplay.PolarAxes.PolarAxisTitleVisibility = 1
foamfoamDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
foamfoamDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
foamfoamDisplay.PolarAxes.PolarLabelVisibility = 1
foamfoamDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
foamfoamDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
foamfoamDisplay.PolarAxes.RadialLabelVisibility = 1
foamfoamDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
foamfoamDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
foamfoamDisplay.PolarAxes.RadialUnitsVisibility = 1
foamfoamDisplay.PolarAxes.ScreenSize = 10.0
foamfoamDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
foamfoamDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
foamfoamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
foamfoamDisplay.PolarAxes.PolarAxisTitleBold = 0
foamfoamDisplay.PolarAxes.PolarAxisTitleItalic = 0
foamfoamDisplay.PolarAxes.PolarAxisTitleShadow = 0
foamfoamDisplay.PolarAxes.PolarAxisTitleFontSize = 12
foamfoamDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
foamfoamDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
foamfoamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
foamfoamDisplay.PolarAxes.PolarAxisLabelBold = 0
foamfoamDisplay.PolarAxes.PolarAxisLabelItalic = 0
foamfoamDisplay.PolarAxes.PolarAxisLabelShadow = 0
foamfoamDisplay.PolarAxes.PolarAxisLabelFontSize = 12
foamfoamDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
foamfoamDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
foamfoamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
foamfoamDisplay.PolarAxes.LastRadialAxisTextBold = 0
foamfoamDisplay.PolarAxes.LastRadialAxisTextItalic = 0
foamfoamDisplay.PolarAxes.LastRadialAxisTextShadow = 0
foamfoamDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
foamfoamDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
foamfoamDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
foamfoamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
foamfoamDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
foamfoamDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
foamfoamDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
foamfoamDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
foamfoamDisplay.PolarAxes.EnableDistanceLOD = 1
foamfoamDisplay.PolarAxes.DistanceLODThreshold = 0.7
foamfoamDisplay.PolarAxes.EnableViewAngleLOD = 1
foamfoamDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
foamfoamDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
foamfoamDisplay.PolarAxes.PolarTicksVisibility = 1
foamfoamDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
foamfoamDisplay.PolarAxes.TickLocation = 'Both'
foamfoamDisplay.PolarAxes.AxisTickVisibility = 1
foamfoamDisplay.PolarAxes.AxisMinorTickVisibility = 0
foamfoamDisplay.PolarAxes.ArcTickVisibility = 1
foamfoamDisplay.PolarAxes.ArcMinorTickVisibility = 0
foamfoamDisplay.PolarAxes.DeltaAngleMajor = 10.0
foamfoamDisplay.PolarAxes.DeltaAngleMinor = 5.0
foamfoamDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
foamfoamDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
foamfoamDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
foamfoamDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
foamfoamDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
foamfoamDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
foamfoamDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
foamfoamDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
foamfoamDisplay.PolarAxes.ArcMajorTickSize = 0.0
foamfoamDisplay.PolarAxes.ArcTickRatioSize = 0.3
foamfoamDisplay.PolarAxes.ArcMajorTickThickness = 1.0
foamfoamDisplay.PolarAxes.ArcTickRatioThickness = 0.5
foamfoamDisplay.PolarAxes.Use2DMode = 0
foamfoamDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
foamfoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on animationScene1
animationScene1.AnimationTime = 2000.0

# turn off scalar coloring
ColorBy(foamfoamDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# change representation type
foamfoamDisplay.SetRepresentationType('Surface With Edges')

# Properties modified on foamfoamDisplay
foamfoamDisplay.EdgeColor = [0.0, 0.0, 0.0]

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1612, 804)

# current camera placement for renderView1
renderView1.CameraPosition = [0, 0.0940167161085186, 110.34910626658501]
renderView1.CameraFocalPoint = [0, 0.0940167161085186, 1.0499999821186066]
renderView1.CameraParallelScale = 0.17582593151360776
renderView1.CameraParallelProjection = 1

# save screenshot
SaveScreenshot('D:/Skole/Uni/ExternalFlow/dashWebApp/assets/10/mesh3.png', renderView1, ImageResolution=[3000, 3000],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='3',
    MetaData=['Application', 'ParaView'])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1612, 804)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.9880642144781314, 0.0940167161085186, 110.34910626658501]
renderView1.CameraFocalPoint = [-0.9880642144781314, 0.0940167161085186, 1.0499999821186066]
renderView1.CameraParallelScale = 0.17582593151360776
renderView1.CameraParallelProjection = 1

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).