function getLinkedHydrogenAtoms(node)
{
	var result = [];
	var siblings = node.getLinkedSiblings();
	siblings.forEach(function(sibling){
		if (sibling.getAtomicNumber && sibling.getAtomicNumber() === 1)  // is H atom
			result.push(sibling);
  });
	return result;
}

function getAromaticDetails(molData, dataFormat)
{	
	var mol = Kekule.IO.loadFormatData(molData, dataFormat || Kekule.IO.DataFormat.MOL);	
	if (mol)
	{
		var aromaticRings = mol.findAromaticRings(true, mol.findAllRings());
    	if (aromaticRings && aromaticRings.length)
		{
			var aromaticGroup = [];
			// iterate each ring and each node on the ring
			aromaticRings.forEach(function(ring){
				var aromaticNodes = [];
				ring.nodes.forEach(function(node){
					aromaticNodes.push(node);
					var hydrogens = getLinkedHydrogenAtoms(node);
					aromaticNodes = aromaticNodes.concat(hydrogens);
				});
				aromaticGroup.push(aromaticNodes);
			});			
				  
			var result = [];
			aromaticGroup.forEach(function(aromaticNodes){
				var resultGroup = [];
				aromaticNodes.forEach(function(node){
					var symbol = node.getSymbol? node.getSymbol(): node.getClassName();
					var coord = node.getCoord3D() || node.getCoord2D();
					resultGroup.push({'symbol': symbol, 'coord': coord});
				});
				result.push(resultGroup);
			});			
		}
		return result;
	}	
	return null;
}

function getAromaticDetailsJsonStr(molData, dataFormat)
{
	var result = getAromaticDetails(molData, dataFormat);	
	if (result)
		return JSON.stringify(result);
	else
		return '';
}